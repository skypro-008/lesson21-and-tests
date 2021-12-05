class Storage:
    goods_quantity = 10

    def __init__(self, qnt: int):
        if qnt < self._get_total():
            self._set_total(self._get_total() - qnt)
            self.goods_quantity = qnt
        else:
            self.goods_quantity = self._get_total()
            self._set_total(0)

    @classmethod
    def _get_total(cls) -> int:
        return cls.goods_quantity

    @classmethod
    def _set_total(cls, qnt):
        cls.goods_quantity = qnt
    
    def more(self, qnt: int):
        self.goods_quantity += qnt
    
    def less(self, qnt: int):
        if self.goods_quantity < qnt:
            return False
        else:
            self.goods_quantity -= qnt

    def fullfill(self):
        total = self._get_total()
        self.more(total)
        self._set_total(0)