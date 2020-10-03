# Youtube Search API -  [Website](http://ec2-54-92-160-125.compute-1.amazonaws.com)

## How it Works?
In search.py, the search.list method has been called to retrieve results matching the specified query term and also the video.list
method to retrieve the statistics belonging to a particular video id. The data thus obtained is getting stored in the database and then pulled on to the index page
using python inbuilt API with the use of django querysets. On the server, a cron job has been setup to call the youtube api in every 15mins, so to fetch the latest videos
user has to refresh the page. The videos are displayed in a paginated response by using django paginator which splits querysets into page objects

## Tech Stack Used

- Python 3.6+
- Django 2.2
- Nginx
- AWS EC2 (for hosting)

## Test Locally

- `git clone https://github.com/ag602/Youtube-Search-API.git`
- `cd Youtube-Search-API`
- `Make virtual env`
- `pip install -r requirements.txt`
- `python3 manage.py makemigrations` and `python3 manage.py migrate`
- In the project root, run the script(for manual testing) - `python search.py`
- `python manage.py runserver`

## How to run on server?

1. Host the website(here I have used a AWS EC2 instance)
2. To set up a cronjob, use this command(on linux):
    - `crontab -e`
    - `Select nano editor [1]`
    - Enter - `*/15 * * * *  $PYTHONPATH $FILEPATH`
    - Enter full PYTHONPATH (after entering in your virtualenv type 'which python' on your terminal)
    - Enter full FILEPATH
    - Ctrl+O and then Ctrl+X to write and exit file

## Future Work

- Add filtering options - sort by view count, rating, etc
- Add iframe for embedding videos on the website itself
- Adding Support for Multiple API Keys
- Adding support for automatic refresh when new items are added to database
- Make UI smooth