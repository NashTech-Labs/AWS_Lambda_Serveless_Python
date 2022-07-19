# Serverless Framework AWS Python 

This template demonstrates how to deploy a Python function running on AWS Lambda using the traditional Serverless Framework. The deployed function does not include any event definitions as well as any kind of persistence (database).

*************************************************************************************************************
## Requirements : 
*************************************************************************************************************
1. Account on AWS and Basic AWS Lambda Understanding
2. Create AWS User with exceution access 
3. Serverless installed on system
4. register with serverless
5. Provide AWS Access Role

### Ways to install serverless

#### 1 : using NPM

* install npm on system
```
$ sudo apt install npm 
```
* install serverless
```
npm install -g serverless
```
#### 2 : using bash script available online

```
curl -o- -L https://slss.io/install | bash
```

### Registration
```
$ serveless

Onboarding "aws-knoldus-project" to the Serverless Dashboard

? Do you want to login/register to Serverless Dashboard? Yes
Logging into the Serverless Dashboard via the browser
If your browser does not open automatically, please open this URL:
https://app.serverless.com?client=cli&transactionId=_hA7xE2E_MgimeYxwVsen

✔ You are now logged into the Serverless Dashboard

```
* On dashboard, in provider add Access Key and  Secret Key for the User

### access role 

* either start same way as before or serverless deploy
```
$ serveless

Onboarding "aws-knoldus-project" to the Serverless Dashboard

? Do you want to login/register to Serverless Dashboard? Yes
Logging into the Serverless Dashboard via the browser
If your browser does not open automatically, please open this URL:
https://app.serverless.com?client=cli&transactionId=_hA7xE2E_MgimeYxwVsen

✔ You are now logged into the Serverless Dashboard
? What org do you want to add this service to? vaibhavkuma779

✔ Your project is ready to be deployed to Serverless Dashboard (org: "vaibhavkuma779", app: "aws-knoldus-project")

? No AWS credentials found, what credentials do you want to use? (Use arrow keys)
❯ AWS Access Role (most secure) 
  Local AWS Access Keys 
  Skip 

? No AWS credentials found, what credentials do you want to use? AWS Access Role (most secure)

If your browser does not open automatically, please open this URL: https://app.serverless.com/vaibhavkuma779/settings/providers?source=cli&providerId=new&provider=aws

To learn more about providers, visit: http://slss.io/add-providers-dashboard
? 
 [If you encountered an issue when setting up a provider, you may press Enter to skip this step] 

⠏ Waiting for creation of AWS Access Role provider

```
*************************************************************************************************************

## Usage

### Deployment

In order to deploy the example, you need to run the following command:

```
$ serverless deploy
```

After running deploy, you should see output similar to:

```bash
Deploying aws-python-project to stage dev (us-east-1)

✔ Service deployed to stack aws-python-project-dev (112s)

functions:
  hello: aws-python-project-dev-hello (1.5 kB)
```

### Invocation

After successful deployment, you can invoke the deployed function by using the following command:

```bash
serverless invoke --function check_connection
```

Which should result in response similar to the following:

```json
{
    "statusCode": 200,
    "body": "{\"message\": \"Go Serverless v3.0! Your function executed successfully!\", \"input\": {}}"
}
```

### Local development

You can invoke your function locally by using the following command:

```bash
serverless invoke local --function hello
```

Which should result in response similar to the following:

```
{
    "statusCode": 200,
    "body": "{\"message\": \"Go Serverless v3.0! Your function executed successfully!\", \"input\": {}}"
}
```
*************************************************************************************************************

### Bundling dependencies

In case you would like to include third-party dependencies, you will need to use a plugin called `serverless-python-requirements`. You can set it up by running the following command:

```bash
serverless plugin install -n serverless-python-requirements
```

Running the above will automatically add `serverless-python-requirements` to `plugins` section in your `serverless.yml` file and add it as a `devDependency` to `package.json` file. The `package.json` file will be automatically created if it doesn't exist beforehand. Now you will be able to add your dependencies to `requirements.txt` file (`Pipfile` and `pyproject.toml` is also supported but requires additional configuration) and they will be automatically injected to Lambda package during build process. For more details about the plugin's configuration, please refer to [official documentation](https://github.com/UnitedIncome/serverless-python-requirements).