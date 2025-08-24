# NetflixInTheMaking

A video streaming platform inspired by Netflix. This project allows users to deploy their own streaming service on AWS using Terraform.

---

## Description

This project helps you build a scalable, cloud-based video streaming platform. Users manage their own AWS credentials through GitLab secret variables. The deployment pipeline leverages Terraform to **validate**, **plan**, and **apply** infrastructure changes, with the Terraform state securely stored in an **S3 bucket**.

**Key Features:**  
- AWS-based video streaming infrastructure  
- Terraform-driven CI/CD pipeline  
- State management in S3 for collaboration and persistence  
- Fully configurable by the user  

---

## Requirements

- AWS account  
- GitLab account  
- Terraform installed locally or in GitLab CI/CD environment  
- AWS credentials stored in GitLab secret variables (`AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`)  

---

## Installation & Deployment

1. **Fork or clone the repository**  
   ```bash
   git clone https://gitlab.com/netflix8065034/netflix-in-the-making.git
   cd netflix-in-the-making
