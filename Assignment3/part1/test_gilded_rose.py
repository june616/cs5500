# -*- coding: utf-8 -*-
import unittest
from gilded_rose import Item, GildedRose, StandardQualityHandler, ConjuredQualityHandler, AgedBrieQualityHandler, BackstageQualityHandler, SulfurasQualityHandler


class TestGildedRose(unittest.TestCase):
    def setUp(self):
        self.items = [
            Item(name="Standard Item", sell_in=10, quality=20),
            Item(name="Conjured", sell_in=5, quality=10),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Backstage passes to a TAFKAL80ETC concert",
                 sell_in=15, quality=20),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        ]
        self.gilded_rose = GildedRose(self.items)

    def test_standard_item(self):
        self.gilded_rose.update_quality()
        self.assertEqual(self.items[0].quality, 19)
        self.assertEqual(self.items[0].sell_in, 9)

    def test_conjured_item(self):
        self.gilded_rose.update_quality()
        self.assertEqual(self.items[1].quality, 8)
        self.assertEqual(self.items[1].sell_in, 4)

    def test_aged_brie(self):
        self.gilded_rose.update_quality()
        self.assertEqual(self.items[2].quality, 1)
        self.assertEqual(self.items[2].sell_in, 1)

    def test_backstage_pass(self):
        self.gilded_rose.update_quality()
        self.assertEqual(self.items[3].quality, 21)
        self.assertEqual(self.items[3].sell_in, 14)

    def test_sulfuras(self):
        self.gilded_rose.update_quality()
        self.assertEqual(self.items[4].quality, 80)
        self.assertEqual(self.items[4].sell_in, 0)

    def test_quality_never_negative(self):
        self.items[0].quality = 0
        self.gilded_rose.update_quality()
        self.assertEqual(self.items[0].quality, 0)

    def test_quality_never_more_than_fifty(self):
        self.items[2].quality = 50
        self.gilded_rose.update_quality()
        self.assertEqual(self.items[2].quality, 50)

    def test_backstage_pass_quality_increase(self):
        self.items[3].sell_in = 5
        self.gilded_rose.update_quality()
        self.assertEqual(self.items[3].quality, 23)

    def test_backstage_pass_quality_drop_after_concert(self):
        self.items[3].sell_in = 0
        self.gilded_rose.update_quality()
        self.assertEqual(self.items[3].quality, 0)


if __name__ == '__main__':
    unittest.main()
