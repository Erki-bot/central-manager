def test():
    import ufirestore.ufirestore as firebase
    from ufirestore.json import FirebaseJson
    
    #Project parameters
    project_id = "central-manager-4d063"
    access_token = "eBPNBaykjlFBDmX60pp1Fm8Hj3ZoMB6odps2hcIA"

    #firebase configuration
    firebase.set_project_id(project_id)
    firebase.set_access_token(access_token)
    doc = FirebaseJson()
    doc.set("age/integerValue", 21)
    response = ufirestore.patch("users/234", doc, ["age"], False)
    print(response)

