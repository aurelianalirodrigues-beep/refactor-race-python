ORDERS_PROCESSED = []

MAX_DISCOUNT_RATE = 0.25
EXPRESS_SHIPPING_MULTIPLIER = 1.8

TAX_RATES = {
    "MG": 0.07,
    "SP": 0.09,
    "RJ": 0.08,
    "ES": 0.07,
}

SOUTHEAST_STATES = {"MG", "SP", "RJ", "ES"}


def calculate_subtotal(items):
    return sum(
        item["price"] * item["qty"]
        for item in items
        if item["qty"] > 0
    )


def calculate_customer_discount(customer_type, subtotal):
    if customer_type == "vip":
        return subtotal * (0.15 if subtotal >= 1000 else 0.10)

    if customer_type == "employee":
        return subtotal * 0.20

    if customer_type == "regular" and subtotal >= 800:
        return subtotal * 0.05

    return 0


def calculate_coupon_discount(coupon, customer_type, subtotal):
    if coupon == "PROMO10":
        return subtotal * 0.10

    if coupon == "PROMO20" and subtotal >= 500:
        return subtotal * 0.20

    if coupon == "VIP50" and customer_type == "vip":
        return 50

    return 0


def calculate_discount(customer, subtotal, coupon):
    discount = calculate_customer_discount(customer["type"], subtotal)
    discount += calculate_coupon_discount(
        coupon,
        customer["type"],
        subtotal,
    )

    return min(discount, subtotal * MAX_DISCOUNT_RATE)


def calculate_weight(items):
    return sum(
        item.get("weight", 0) * item["qty"]
        for item in items
    )


def calculate_shipping(subtotal, weight, state, express):
    if subtotal >= 500 and not express:
        return 0

    if state in SOUTHEAST_STATES:
        shipping = 20 + weight * 0.4
    else:
        shipping = 35 + weight * 0.6

    if express:
        shipping *= EXPRESS_SHIPPING_MULTIPLIER

    return shipping


def calculate_tax(value_after_discount, state):
    tax_rate = TAX_RATES.get(state, 0.12)
    return value_after_discount * tax_rate


def calculate_points(customer_type, total):
    divisor = 5 if customer_type == "vip" else 10
    return int(total / divisor)


def find_duplicate_products(items):
    seen = set()
    duplicates = []

    for item in items:
        name = item["name"]

        if name in seen and name not in duplicates:
            duplicates.append(name)

        seen.add(name)

    return duplicates


def process_order(customer, items, coupon="", state="MG", express=False):
    subtotal = calculate_subtotal(items)

    discount = calculate_discount(
        customer,
        subtotal,
        coupon,
    )

    value_after_discount = subtotal - discount

    weight = calculate_weight(items)

    shipping = calculate_shipping(
        subtotal,
        weight,
        state,
        express,
    )

    tax = calculate_tax(
        value_after_discount,
        state,
    )

    total = round(
        value_after_discount + shipping + tax,
        2,
    )

    points = calculate_points(
        customer["type"],
        value_after_discount + shipping + tax,
    )

    duplicate_products = find_duplicate_products(items)

    result = {
        "customer": customer["name"],
        "subtotal": round(subtotal, 2),
        "discount": round(discount, 2),
        "shipping": round(shipping, 2),
        "tax": round(tax, 2),
        "total": total,
        "points": points,
        "duplicate_products": duplicate_products,
    }

    ORDERS_PROCESSED.append(result)

    print("Pedido processado para " + customer["name"])
    print("Subtotal:", subtotal)
    print("Desconto:", discount)
    print("Frete:", shipping)
    print("Imposto:", tax)
    print("TOTAL:", total)

    return result