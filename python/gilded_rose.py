# -*- coding: utf-8 -*-

class GildedRose(object):

    # Default constructor
    def __init__(self, items):
        self.items = items

    # Maintains and updates quality for all items
    def update_quality(self):
        for item in self.items:
            # Sulfuras
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            # Aged Brie
            elif item.name == "Aged Brie":
                item.quality += 1
                if item.sell_in <= 0:  # If the sell by date has passed
                    item.quality += 1

            # Backstage passes
            elif "Backstage passes" in item.name:
                if item.sell_in <= 0:
                    item.quality = 0
                elif item.sell_in <= 5:
                    item.quality += 3
                elif item.sell_in <= 10:
                    item.quality += 2
                else:
                    item.quality += 1

            # Conjured items
            elif "Conjured" in item.name:
                item.quality -= 2
                if item.sell_in <= 0:
                    item.quality -= 2

            # Miscellaneous items
            else:
                item.quality -= 1
                if item.sell_in <= 0:
                    item.quality -= 1

            # Quality restriction
            if item.quality < 0:
                item.quality = 0
            elif item.quality > 50:
                item.quality = 50

            # Decrement # of days to sell the item
            item.sell_in -= 1
         
# Default constructor
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
