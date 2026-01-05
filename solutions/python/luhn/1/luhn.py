class Luhn:
    def __init__(self, card_num):
        self.card_num = ''.join(ch if ch != " " else "" for ch in card_num)

    def valid(self):
        card_num = self.card_num
        if len(card_num) <= 1 or not card_num.isdigit():
            return False
        
        unchanged = list(card_num[-1::-2])
        print(unchanged)
        u = list(map(int, unchanged))
        part_one = sum(u)

        changed = list(card_num[-2::-2])
        print(changed)
        c = [int(x)*2-9 if int(x)*2 > 9 else int(x)*2 for x in changed]
        part_two = sum(c)


        return (part_one + part_two) % 10 == 0

        

        

        
