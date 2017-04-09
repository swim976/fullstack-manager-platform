FROM python:3.6

# fullstack-manager-platform dockerfile
# command: docker run -it --name admin --net host --add-host="mariadb:127.0.0.1" -p 8000:8000
 -v /c/Users/haofly/workspace/fullstack-manager-platform:/usr/src/app -d admin
# 不用挂载的方式就不能实时更新文件，md


MAINTAINER haofly <haoflynet@gmail.com>


RUN mkdir -p /usr/src/app
RUN mkdir -p /data/backup/mysql
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
COPY . /usr/src/app

RUN apt-get update && apt-get install -y \
				rsyslog \ 
				cron \
				vim \
				gcc \
				gettext \
				mysql-client libmysqlclient-dev \
				sqlite3 \
		--no-install-recommends && rm -rf /var/lib/apt/lists/*

RUN rsyslogd
RUN cron
RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py crontab add

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
