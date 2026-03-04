# This is the project WITH the bug – what to do next

You use **this folder** (`flaskAppWithbugasignmet1`) for the whole assignment. It is already the **same** GitHub repo as [MatthewRInnes/DevOpsassignement1](https://github.com/MatthewRInnes/DevOpsassignement1) – same project, same history. The bug is in **app.py** line 42: `return -pounds_to_kg(value)` (the minus makes pounds→kg wrong).

---

## 1. Do Lab 4 on this project

- Open **LAB4_THREE_STEPS.md** from your other folder (FlaskAppweighttofixv1) and do **Step 1** in **this** folder:
  - In **app.py**: change the last line to  
    `app.run(host='0.0.0.0', port=8080, debug=False)`
  - In **requirements.txt**: add `gunicorn==20.0.4`
  - Create **Dockerfile**, **docker-compose.yml**, and **nginx** folder + **nginx.conf** (copy the content from LAB4_THREE_STEPS.md).
- Then do **Step 2** in this folder:  
  `docker compose up --build -d` → check http://localhost/ → `docker compose down` → push to GitHub (e.g. branch `week_4_lab`).

---

## 2. Do Lab 5 (Jenkins on EC2)

- Use **this** repo on GitHub for Jenkins.
- EC2, Jenkins, pipeline: tests then Docker build (and push to Docker Hub if required).
- In Jenkins build steps, run from the **project root** (no `cd flask-app`), because this project has no `flask-app` subfolder.

---

## 3. Do Task 5 (incident + report photos)

- Create a **feature branch**.
- Add a **new test** in **tests/test_app.py** that checks the main function for pounds→kg, for example:

  ```python
  from app import main_conversion_function

  def test_pounds_to_kg_main_function():
      result = main_conversion_function(1, 'pounds', 'kg')
      expected = 0.453592
      assert result == pytest.approx(expected, rel=1e-5)
  ```

- Commit and push **only the test** (do not fix the bug yet). Jenkins should **fail** → take **Photo 1 and 2** (console + error).
- Then in **app.py** change line 42 from `return -pounds_to_kg(value)` to `return pounds_to_kg(value)`, commit and push. Jenkins should **pass** → take **Photo 3** (Git/GitHub with the fix commit) and note the **commit hash** for the report.

---

## 4. Report and practical

- Put **Photo 1, 2, 3** and the **commit hash** in your written report.
- Do the video and evidence document using this repo and the same incident (pounds→kg bug).

---

**Summary:** This folder = project with the bug. Do Lab 4 here, then Lab 5 with this repo, then Task 5 (add test → fail → fix → pass) and the report/video.
