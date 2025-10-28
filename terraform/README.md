# trainings
Devopsfarm Training content


# EC2 machine for FE
# RDS instance
# Lambda

.tf
.tfvars
.tmlp


Commands
terraform init
    initialize your terraform directory with pre-requiresits
        download providers
        backend initiliaze (by default it is local and file based)
terraform plan (read only operation)

    -- shows current state of the infrastructure
    -- shows what will be changed when you apply the terraform scripts


terraform apply (read + write)
    -- creats plan and apply after approval