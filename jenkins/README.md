# Jenkins Overview

1. CI-CD
2. WHy jenkins?
3. Installation -- using docker https://hub.docker.com/r/jenkins/jenkins
   ```
   docker run -p 8080:8080 -p 50000:50000 --restart=on-failure jenkins/jenkins:lts-jdk17
   ```
4. UI Overview
5. Freestyle Job
6. Jenkins agent
7. Pipeline Job
8. Jenkins Agents(dynamic agents + static agents)
9. Configuration(users/tools/Environment/Plugnings)




Handson

Create user
Login
Create folder for your user
Create hello world job -- job should print Hello world in console
```
echo "hello world"
```

Created a job with parameters(string boolean and Choices)

Create a job that checkout code, build and tests. Post build, It publishes the tests reports in the build

Create a declarative pipeline job from https://github.com/DevopsFarmer/java-sample-app.git that will do
Four stages
  checkout
  build
  test
  publish

Add parameters to enable/disable test stage

