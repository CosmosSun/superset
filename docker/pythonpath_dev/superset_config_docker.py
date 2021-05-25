#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

#
# This is an example "local" configuration file. In order to set/override config
# options that ONLY apply to your local environment, simply copy/rename this file
# to docker/pythonpath/superset_config_docker.py
# It ends up being imported by docker/superset_config.py which is loaded by
# superset/config.py
#

#SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://pguser:pgpwd@some.host/superset"
#SQLALCHEMY_ECHO = True

# Email configuration
ALERT_REPORTS_NOTIFICATION_DRY_RUN = False
SMTP_HOST = "smtp.qq.com" #change to your host
SMTP_STARTTLS = False     #qq mail not support STARTTLS
SMTP_SSL = True           #qq mail must SSL
SMTP_USER = "10xxxx"
SMTP_PORT = 465 # your port eg. 587
SMTP_PASSWORD = "yyyy"
SMTP_MAIL_FROM = "10xxxx@qq.com"

# WebDriver configuration
# If you use Firefox, you can stick with default values
# If you use Chrome, then add the following WEBDRIVER_TYPE and WEBDRIVER_OPTION_ARGS
WEBDRIVER_TYPE = "chrome"
WEBDRIVER_OPTION_ARGS = [
    "--force-device-scale-factor=2.0",
    "--high-dpi-support=2.0",
    "--headless",
    "--disable-gpu",
    "--disable-dev-shm-usage",
    "--no-sandbox",
    "--disable-setuid-sandbox",
    "--disable-extensions",
]

# Window size - this will impact the rendering of the data
WEBDRIVER_WINDOW = {"dashboard": (3000, 2000), "slice": (3000, 1200)}
