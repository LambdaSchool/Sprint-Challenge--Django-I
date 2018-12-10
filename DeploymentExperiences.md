
- A link to your [Countries project repo](https://github.com/timh1203/lsw19i-ii-introDjango)
- A link to your [Live site: admin](https://travelous.herokuapp.com/admin)
- A link to your [Live site: countries](https://travelous.herokuapp.com/api/countries/)

- Summarize the key steps in the deployment process.
  - What went well?
  - **Was able to get everything deployed relatively smoothly except noted errors below.**

  - What challenges did you face?
  - **Ran into `Error while running '$ python manage.py collectstatic --noinput'` error, which I solved by running `heroku config:set DISABLE_COLLECTSTATIC=1`, which disables running the collectstatic command when app is pushed/built.**
  - **Ran into `ModuleNotFoundError: No module named 'corsheaders'` error, which I solved by installing "django-cors-headers" locally and pushed up changes.**

  - How far did you get?
  - **Deployed full app.**


- We have utilized docs from several different projects over the course of this Sprint.
  - Which docs did you think were the most helpful?
  - **The Heroku docs were really helpful in helping me understand the static folder error and also setting config variables**

  - Name one or two specific things about this resource that you think sets it apart from other docs you have referenced in the past.
  - **It is well written with pictures and code snippets. There was also a repo available to see how to do bypass static file problem by adding a static folder to the repo.**
