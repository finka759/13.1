class Product:
    """ Для класса Product:
        название,
        описание,
        цена,
        количество в наличии. """

    prdct_name: str
    prdct_description: str
    prdct_price: int
    prdct_quantity_in_stock: int

    def __init__(self, prdct_name, prdct_description, prdct_price, prdct_quantity_in_stock):
        self.prdct_name = prdct_name
        self.prdct_description = prdct_description
        self.prdct_price = prdct_price
        self.prdct_quantity_in_stock = prdct_quantity_in_stock
