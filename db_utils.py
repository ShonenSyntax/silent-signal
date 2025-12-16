from firebase_admin import firestore

db = firestore.client()

def get_all_reports():
    reports_ref = db.collection("reports")
    docs = reports_ref.order_by("timestamp", direction=firestore.Query.DESCENDING).stream()

    reports = []
    for doc in docs:
        data = doc.to_dict()
        reports.append(data)

    return reports