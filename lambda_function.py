import boto3
import urllib.parse
from datetime import datetime

def get_mediaconvert_client():
    # First get the account-specific endpoint
    mediaconvert = boto3.client("mediaconvert", region_name="eu-west-2")
    endpoints = mediaconvert.describe_endpoints(MaxResults=1)
    endpoint_url = endpoints["Endpoints"][0]["Url"]

    return boto3.client("mediaconvert", endpoint_url=endpoint_url, region_name="eu-west-2")

def lambda_handler(event, context):
    mediaconvert_client = get_mediaconvert_client()
    
    for record in event['Records']:
        # Get bucket and object key from S3 event
        bucket = record['s3']['bucket']['name']
        print("bucket:", bucket)
        key = urllib.parse.unquote_plus(record['s3']['object']['key'])
        
        print(f"Processing file: s3://{bucket}/{key}")
        
        # Create MediaConvert job
        try:
            response = create_mediaconvert_job(mediaconvert_client, bucket, key)
            print(f"Job created successfully: {response['Job']['Id']}")
        except Exception as e:
            print(f"Error creating MediaConvert job: {str(e)}")
            return {'statusCode': 500, 'body': f'Failed to create job: {str(e)}'}
    
    return {'statusCode': 200, 'body': 'Jobs created successfully'}

def create_mediaconvert_job(client, input_bucket, input_key):
    """Create a MediaConvert job for HLS streaming output"""
    output_bucket= 'outputvideonetflix'
    account_id = '417518835809'
    # Generate timestamp for unique naming
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    filename_without_ext = input_key.rsplit('.', 1)[0]  # Remove file extension
    
    # Your specific job settings
    job_settings = {
        "Queue": f"arn:aws:mediaconvert:eu-west-2:{account_id}:queues/Default",
        "UserMetadata": {
            "OriginalFile": f"s3://{input_bucket}/{input_key}",
            "ProcessedAt": timestamp
        },
        "Role": f"arn:aws:iam::{account_id}:role/MediaConvert_Default_Role",
        "Settings": {
            "TimecodeConfig": {
                "Source": "ZEROBASED"
            },
            "OutputGroups": [
                {
                    "CustomName": "1080",
                    "Name": "Apple HLS",
                    "Outputs": [
                        {
                            "ContainerSettings": {
                                "Container": "M3U8",
                                "M3u8Settings": {}
                            },
                            "VideoDescription": {
                                "CodecSettings": {
                                    "Codec": "H_264",
                                    "H264Settings": {
                                        "MaxBitrate": 5000000,
                                        "RateControlMode": "QVBR",
                                        "SceneChangeDetect": "TRANSITION_DETECTION"
                                    }
                                }
                            },
                            "AudioDescriptions": [
                                {
                                    "CodecSettings": {
                                        "Codec": "AAC",
                                        "AacSettings": {
                                            "Bitrate": 96000,
                                            "CodingMode": "CODING_MODE_2_0",
                                            "SampleRate": 48000
                                        }
                                    }
                                }
                            ],
                            "OutputSettings": {
                                "HlsSettings": {}
                            },
                            "NameModifier": "1080"
                        },
                        {
                            "ContainerSettings": {
                                "Container": "M3U8",
                                "M3u8Settings": {}
                            },
                            "VideoDescription": {
                                "Width": 1280,
                                "Height": 720,
                                "CodecSettings": {
                                    "Codec": "H_264",
                                    "H264Settings": {
                                        "MaxBitrate": 2500000,
                                        "RateControlMode": "QVBR",
                                        "SceneChangeDetect": "TRANSITION_DETECTION"
                                    }
                                }
                            },
                            "AudioDescriptions": [
                                {
                                    "CodecSettings": {
                                        "Codec": "AAC",
                                        "AacSettings": {
                                            "Bitrate": 96000,
                                            "CodingMode": "CODING_MODE_2_0",
                                            "SampleRate": 48000
                                        }
                                    }
                                }
                            ],
                            "OutputSettings": {
                                "HlsSettings": {}
                            },
                            "NameModifier": "720"
                        }
                    ],
                    "OutputGroupSettings": {
                        "Type": "HLS_GROUP_SETTINGS",
                        "HlsGroupSettings": {
                            "SegmentLength": 10,
                            "Destination": f"s3://{output_bucket}/{filename_without_ext}_{timestamp}/",
                            "MinSegmentLength": 0
                        }
                    }
                }
            ],
            "FollowSource": 1,
            "Inputs": [
                {
                    "AudioSelectors": {
                        "Audio Selector 1": {
                            "DefaultSelection": "DEFAULT"
                        }
                    },
                    "VideoSelector": {},
                    "TimecodeSource": "ZEROBASED",
                    "FileInput": f"s3://{input_bucket}/{input_key}"
                }
            ]
        },
        "BillingTagsSource": "JOB",
        "AccelerationSettings": {
            "Mode": "DISABLED"
        },
        "StatusUpdateInterval": "SECONDS_60",
        "Priority": 0
    }
    
    # Submit the job
    response = client.create_job(**job_settings)
    print("response:", response)
    return response
