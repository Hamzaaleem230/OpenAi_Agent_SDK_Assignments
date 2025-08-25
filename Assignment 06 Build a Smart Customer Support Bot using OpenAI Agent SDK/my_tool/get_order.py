from agents import function_tool
import logging

# Configure logging
logging.basicConfig(filename='logs/events.log', level=logging.INFO)

# This tool can be used to check the status of an order
@function_tool(is_enabled=True)
def get_order_status(order_id: str) -> str:
    # log every tool call
    logging.info(f"Tool Call: get_order_status({order_id})")
    # check order status
    print("🔎 Checking your orders...")
    if order_id == "1880":
        return f"- 📦 Order {order_id} → In progress."
    if order_id == "1881":
        return f"- 🚚 Order {order_id} → Shipped."
    if order_id == "1882":
        return f"- ✅ Order {order_id} → Delivered."
    else:
        return f"- ⚠️ Sorry 😅, order {order_id} was not found in our system."
