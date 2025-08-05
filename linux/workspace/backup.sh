# coredumps
# javadump

# #developer wants to collect coredumps and javadumps from all machines in the infra

# # assuming the application runs in folder /opt/application/ 
# # they want to collect coredumps (/opt/application/coredumps)
# # they want to collect javadumps (/opt/application/javadumps)
# mkdir send_to_developer
# mv /opt/application/coredumps/* send_to_developer/
# mv /opt/application/javadumps/* send_to_developer/

# # they want to collect system logs (/var/log/application/logs)
# cp /var/log/application/logs/* send_to_developer/
# # application zip file
# tar -czf /opt/application/send_to_developer/application_backup.tar.gz /opt/application/
# # db dump
# pg_dump -U username -h hostname -d dbname > send_to_developer/db_dump.sql

# tar -czf `hostname`_application_backup.tar.gz send_to_developer/
# # they want this in a mail or on some s3 bucket

# aws s3 cp send_to_developer/application_backup.tar.gz s3://your-bucket-name/
# # assuming they want to send this via email
# # using mailx to send the email
# echo "Please find the attached logs and dumps." | mailx -s "Application Logs and Dumps" -a send_to_developer/application_backup.tar.gz -a send_to_developer/db_dump.sql



# cronjob  -- they are schedulers. they runs `something` at `some time`



# # I as devops engineer will run the backup.sh script to collect all the dumps and logs at 6 AM every day
# crontab -e

echo "backup started at $(date)" >> /var/log/backup.log