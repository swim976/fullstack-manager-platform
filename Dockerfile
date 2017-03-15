# fullstack-manager-platform dockerfile
# command: docker run -i -it --name admin -p 8000:8000 --link admin-mariadb:mariadb -v /Users/haofly/workspace/fullstack-manager-platform:/usr/src /app  -d admin


MAINTAINER haofly <haoflynet@gmail.com>

FROM python:3.6

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /usr/src/app

RUN apt-get update && apt-get install -y \
				vim \
				gcc \
				gettext \
				mysql-client libmysqlclient-dev \
				sqlite3 \
		--no-install-recommends && rm -rf /var/lib/apt/lists/*

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]