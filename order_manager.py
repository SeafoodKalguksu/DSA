# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from typing import List

class OrderManager:
    def __init__(self) -> None:
        self.data: List[int] = []

    def place_order(self, order_id: int) -> None:
        self.data.append(order_id)

    def remove_order(self, order_id: int) -> None:
        self.data.remove(order_id)

    def get_order_status(self, order_id: int) -> int:
        if order_id in self.data:
            return self.data.index(order_id) + 1
        else:
            return -1

    def remain_orders(self) -> List[int]:
        return self.data


def main():
    order_system = OrderManager()

    order_system.place_order(2)
    order_system.remove_order(2)
    order_system.place_order(1818)
    order_system.place_order(8282)
    order_system.place_order(2255)
    order_system.place_order(6515)
    order_system.remove_order(1818)
    order_system.place_order(486)

    print(f'order_system.get_order_status(486) = {order_system.get_order_status(486)}')
    print(f'order_system.get_order_status(3) = {order_system.get_order_status(3)}')

    order_system.place_order(4860)
    print(f'remain orders = {order_system.remain_orders()}')


if __name__ == "__main__": # 1 -1 2
    main()
