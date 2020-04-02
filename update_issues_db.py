from issue.create import create
from issue.get import get
import json


issues = [
    {
        "Chamber": "Public",
        "Short Title": "Closing of Travel from Coronavirus Countries",
        "Start Date": "2019-07-22",
        "End Date": "2020-04-30",
        "id": "i0001",
        "Summary":
        "Should the Australian government look to limit travel from countries affected by Coronavirus?",
        "Description":
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        "Sponsor": "Alexanda Great",
        "Yes": 9004,
        "No": 400,
    },
    {
        "Chamber": "Public",
        "Short Title": "GST on Sanitary Items",
        "Start Date": "2019-09-24",
        "End Date": "2020-07-30",
        "id": "i0002",
        "Summary":
        "Should the Australian government legislate to excluse Sanitary and Health items from the GST?",
        "Description":
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        "Sponsor": "Health Lobby Group",
        "Yes": 8004,
        "No": 2070,
    },
    {
        "Chamber": "Public",
        "Short Title": "Legalise Weed",
        "Start Date": "2019-05-06",
        "End Date": "2020-08-30",
        "id": "i0003",
        "Summary":
        "Should the Australian government legalise recreational marijuana nationally?",
        "Description":
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        "Sponsor": "Weed Lobby Group",
        "Yes": 5888,
        "No": 5123,
    },
    {
        "Chamber": "Public",
        "Short Title": "Independent Anti-corruption Commsion",
        "Start Date": "2019-05-01",
        "End Date": "2020-05-30",
        "id": "i0004",
        "Summary": "Should an independent Federal ICAC be created?",
        "Description":
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        "Sponsor": "Freedom Lobby Group",
        "Yes": 9900,
        "No": 100,
    },
]


for issue in issues:
    print(issue)
    create({"body": json.dumps(issue)}, None)
