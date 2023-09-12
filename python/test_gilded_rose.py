# -*- coding: utf-8 -*-
import unittest
from texttest_fixture import simulator
from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    # Test for item creation
    def test_foo(self):
        item_name = "foo"
        item_sell_in = 0
        item_quality = 0

        items = [Item(item_name, item_sell_in, item_quality)]

        self.assertEqual(item_name, items[0].name)
        self.assertEqual(item_sell_in, items[0].sell_in)
        self.assertEqual(item_quality, items[0].quality)

    # Testing Aged Brie, which increases in quality
    def test_aged_brie(self):
        items = [Item("Aged Brie", -1, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(3, items[0].quality)

    # Test sulfuras never loses quality, nor has to be sold (so sell in shouldn't change either)
    def test_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    # Test conjured items should lose quality twice as fast 
    def test_conjured_items(self):
        items = [Item("Conjured Mana Cake", 2, 4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(2, items[0].quality)

    # Tests Backstage passes follows same initial logic to Aged Brie
    def test_backstage_passes(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 12, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(11, items[0].sell_in)
        self.assertEqual(21, items[0].quality)

    # Tests Backstage passes increased in quality by 2 when there are 10 days or less
    def test_backstage_passes_ten_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(22, items[0].quality)

    # Tests Backstage passes increased in quality by 3 when there are 5 days or less
    def test_backstage_passes_five_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(23, items[0].quality)

    # Tests Backstage passes quality drops to 0 after the concert
    def test_backstage_passes_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    # Tests items which do not have any special conditions
    def test_miscellaneous_items(self):
        items = [Item("+5 Dexterity Vest", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(19, items[0].quality)

    # Tests quality decreases twice as fast after the sell by date
    def test_passed_sell_by_date(self):
        items = [Item("+5 Dexterity Vest", 0, 19)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(17, items[0].quality)    

    # Test that we raise an Exception for non integer value for days
    def test_simulator(self):
        self.assertRaises(ValueError, simulator, ["texttest_fixture.py", "11.5"])



if __name__ == '__main__':
    unittest.main()
