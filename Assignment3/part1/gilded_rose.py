# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class QualityHandler:
    def __init__(self, item):
        self.item = item

    def update_quality(self):
        pass


class StandardQualityHandler(QualityHandler):
    def update_quality(self):
        decrement = 1
        if self.item.sell_in <= 0:
            decrement *= 2
        self.item.quality = max(0, self.item.quality - decrement)
        self.item.sell_in -= 1


class ConjuredQualityHandler(QualityHandler):
    def update_quality(self):
        decrement = 2
        if self.item.sell_in <= 0:
            decrement *= 2
        self.item.quality = max(0, self.item.quality - decrement)
        self.item.sell_in -= 1


class AgedBrieQualityHandler(QualityHandler):
    def update_quality(self):
        if self.item.quality < 50:
            self.item.quality += 1
        self.item.sell_in -= 1


class BackstageQualityHandler(QualityHandler):
    def update_quality(self):
        if self.item.quality < 50:
            self.item.quality += 1
            if self.item.sell_in < 11:
                self.item.quality = min(50, self.item.quality + 1)
            if self.item.sell_in < 6:
                self.item.quality = min(50, self.item.quality + 1)
        self.item.sell_in -= 1
        if self.item.sell_in < 0:
            self.item.quality = 0


class SulfurasQualityHandler(QualityHandler):
    def update_quality(self):
        pass  # Sulfuras items do not change


class GildedRose(object):
    item_handler_mapping = {
        'Aged Brie': AgedBrieQualityHandler,
        'Backstage passes to a TAFKAL80ETC concert': BackstageQualityHandler,
        'Sulfuras, Hand of Ragnaros': SulfurasQualityHandler,
        'Conjured': ConjuredQualityHandler
    }

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            handler_class = self.item_handler_mapping.get(
                item.name, StandardQualityHandler)
            handler = handler_class(item)
            handler.update_quality()
        # for item in self.items:
        #     if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
        #         if item.quality > 0:
        #             if item.name != "Sulfuras, Hand of Ragnaros":
        #                 item.quality = item.quality - 1
        #     else:
        #         if item.quality < 50:
        #             item.quality = item.quality + 1
        #             if item.name == "Backstage passes to a TAFKAL80ETC concert":
        #                 if item.sell_in < 11:
        #                     if item.quality < 50:
        #                         item.quality = item.quality + 1
        #                 if item.sell_in < 6:
        #                     if item.quality < 50:
        #                         item.quality = item.quality + 1
        #     if item.name != "Sulfuras, Hand of Ragnaros":
        #         item.sell_in = item.sell_in - 1
        #     if item.sell_in < 0:
        #         if item.name != "Aged Brie":
        #             if item.name != "Backstage passes to a TAFKAL80ETC concert":
        #                 if item.quality > 0:
        #                     if item.name != "Sulfuras, Hand of Ragnaros":
        #                         item.quality = item.quality - 1
        #             else:
        #                 item.quality = item.quality - item.quality
        #         else:
        #             if item.quality < 50:
        #                 item.quality = item.quality + 1
