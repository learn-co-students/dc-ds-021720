royal_num = {'A':1, 'J':10, 'Q':10, 'K':10}
def random_variable(two_cards):
    num1 = 0
    num2 = 0
    card1 = two_cards[0]
    card2 = two_cards[1]
    if card1[1] in royal_num.keys():
        num1 = royal_num[card1[1]]
    else:
        num1 = int(card1[1])
    if card2[1] in royal_num.keys():
        num2 = royal_num[card2[1]]
    else:
        num2 = int(card2[1])
    return num1 + num2
card_index = np.random.choice(range(1300),1)[0]
print(sample_space[card_index])
random_variable(sample_space[card_index])


all_values = [random_variable(a) for a in sample_space ]


import collections
counter = collections.Counter(all_values)

# Convert frequency to probability - divide each frequency value by total number of values
pmf = []
for key, val in counter.items():
    pmf.append(round(val / len(all_values), 4))

print(counter.keys(), pmf)


x = np.unique(all_values, return_counts=True)[0]
y = np.cumsum(np.unique(all_values, return_counts=True)[1])/len(all_values)
plt.plot(x,y, marker = '.',linestyle = 'none')
plt.show()