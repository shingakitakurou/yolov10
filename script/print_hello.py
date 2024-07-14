
api_token = {"username":"shingaki0926","key":"0c253d04a451be74f57e43823c0a5f22"}

import json

with open('/root/.kaggle/kaggle.json', 'w') as file:
    json.dump(api_token, file)

# !chmod 600 ~/.kaggle/kaggle.json