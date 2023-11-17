
def total_carrito (request):
    total = 0
    totitem = 0
    if request.user.is_authenticated:
        if request.session.get("carrito"):
            for key , value in request.session["carrito"].items():
                total += float(value["acumulado"])
                totitem += 1
    return {"total_carrito" : total,
            "total_items" : totitem}                           