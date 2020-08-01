# import gspread
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build

scope = ['https://www.googleapis.com/auth/documents.readonly',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

# scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)

DOCUMENT_ID = ''

service = build('docs', 'v1', credentials=creds)

# Retrieve the documents contents from the Docs service.
document = service.documents().get(documentId=DOCUMENT_ID).execute()

# print('The title of the document is: {}'.format(document.get('title')))

# requests = [
#          {
#             'insertText': {
#                 'location': {
#                     'index': 1,
#
#                 },
#                 'text': '\n'+'text5'+' '
#             }
#         },
#           {
#             'insertText': {
#                 'location': {
#                     'index': 8,
#
#                 },
#                 'text': 'text6'
#             }
#         }
#
#     ]
#
# result = service.documents().batchUpdate(documentId=DOCUMENT_ID, body={'requests': requests}).execute()

# Insert a table at the end of the body.
# (An empty or unspecified segmentId field indicates the document's body.)

# requests = [{
#     'insertTable': {
#         'rows': 3,
#         'columns': 3,
#         'endOfSegmentLocation': {
#             'segmentId': ''
#         }
#     },
# }
# ]



# result = service.documents().batchUpdate(documentId=DOCUMENT_ID, body={'requests': requests}).execute()


# requests = [{
#     'insertTable': {
#         'rows': 3,
#         'columns': 3,
#         'endOfSegmentLocation': {
#             'segmentId': ''
#         }
#     },
# },
# ]
#
# result = service.documents().batchUpdate(documentId=DOCUMENT_ID, body={'requests': requests}).execute()
# requests = [
#     {
#         'insertText': {
#             'location': {
#                 'index': 1,
#             },
#             'text': 'text1'
#         }
#     },
#     {
#         'insertText': {
#             'location': {
#                 'index': 6,
#             },
#             'text': 'text2'
#         }
#     },
#     {
#         'insertText': {
#             'location': {
#                 'index': 11,
#             },
#             'text': 'text3'
#         }
#     },
# ]



# requests = [
#         {
#           "insertTable":
#           {
#             "endOfSegmentLocation":
#             {
#               "segmentId": ""
#             },
#             "columns": 2,
#             "rows": 2
#           }
#         },
#         {
#           "insertText":
#           {
#             "location":
#             {
#               "index": 5
#             },
#             "text": "Cell content"
#           }
#         },{
#           "insertText":
#           {
#             "location":
#             {
#               "index": 19
#             },
#             "text": "Cell content"
#           }
#         },{
#           "insertText":
#           {
#             "location":
#             {
#               "index": 32
#             },
#             "text": "Cell content"
#           }
#         }
#
#       ]



# requests = [
#     {
#         "insertTable":
#         {
#             "rows": 3,
#             "columns": 2,
#             "location":
#             {
#                 "index": 1
#             }
#         }
#     }, {
#         "insertText":
#         {
#             "text": "24",
#             "location":
#             {
#                 "index": 17
#             }
#         }
#     },
#     {
#         "insertText":
#         {
#             "text": "new",
#             "location":
#             {
#                 "index": 15
#             }
#         }
#     },
#     {
#         "insertText":
#         {
#             "text": "12",
#             "location":
#             {
#                 "index": 12
#             }
#         }
#     },
#     {
#         "insertText":
#         {
#             "text": "dentist",
#             "location":
#             {
#                 "index": 10
#             }
#         }
#     },
#     {
#         "insertText":
#         {
#             "text": "rank",
#             "location":
#             {
#                 "index": 7
#             }
#         }
#     },
#     {
#         "insertText":
#         {
#             "text": "name",
#             "location":
#             {
#                 "index": 5
#             }
#         }
#     }
# ]
# result = service.documents().batchUpdate(
#     documentId=DOCUMENT_ID, body={'requests': requests}).execute()


row=4
col=2
requests = [
    {
        "insertTable":
        {
            "rows": row,
            "columns": col,
            "location":
            {
                "index": 1
            }
        }
    },
]

result = service.documents().batchUpdate(documentId=DOCUMENT_ID, body={'requests': requests}).execute()

# requests = [
#
#     {
#         "insertText":
#         {
#             "text": "B2",
#             "location":
#             {
#                 "index": 12
#             }
#         }
#     },
#     {
#         "insertText":
#         {
#             "text": "A2",
#             "location":
#             {
#                 "index": 10
#             }
#         }
#     },
#     {
#         "insertText":
#         {
#             "text": "B1",
#             "location":
#             {
#                 "index": 7
#             }
#         }
#     },
#     {
#         "insertText":
#         {
#             "text": "A1",
#             "location":
#             {
#                 "index": 5
#             }
#         }
#     }
# ]
#
# result = service.documents().batchUpdate(documentId=DOCUMENT_ID, body={'requests': requests}).execute()


# lis=[12,10,7,5]
# arr=['B2','A2','RANK','KEYWORD']
arr = ['4', 'new york dentist', 'NA', 'dentist near York, UK', 'NA', 'dentist near york', 'RANK', 'KEYWORD']
lis = [22, 20, 17, 15, 12, 10, 7, 5]

for idx,l in enumerate(lis):
    requests = [
        {
            "insertText":
                {
                    "text": arr[idx],
                    "location":
                        {
                            "index": l
                        }
                }
        }
    ]

    result = service.documents().batchUpdate(documentId=DOCUMENT_ID, body={'requests': requests}).execute()

print('\n'*2)
print(result)
print('\n'*2)