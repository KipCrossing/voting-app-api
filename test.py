# from user.create import create
# from issue.get import get
# import json
from update_results_db import run

run(None, None)

# print(create({"body": json.dumps(
#     {"First Name": "Bob", "Last Name": "Katter", "Age": 58, "Sex": "M", "Location": "Sydney"}
# )}, None))


# print(get({"pathParameters":
#            {
#                "id": "i0003"
#            }}, None))
