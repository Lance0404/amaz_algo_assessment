"""
requirement:
1. get the existence count of competitor accumulated in all the reviews
2. return the number of `topNCompetitors` of competitors with the largest count in desc order
3. if counts are the same, name should be sorted in alphabetic asec order

todo list:
1. doesn't support case insensitive search yet
2. try to make it more efficient
"""


def findTopNCompetitors(numCompetitors, topNCompetitors, competitors, numReviews, reviews):
    competitor_uniq_cnt = {}
    for i in range(numCompetitors):
        if competitors[i] not in competitor_uniq_cnt:
            competitor_uniq_cnt[competitors[i]] = 0
        for j in range(numReviews):
            if competitors[i] in reviews[j]:
                competitor_uniq_cnt[competitors[i]] += 1

    # reverse the key count order in the tuple
    competitor_uniq_cnt_lst = [(count, name) for name, count in competitor_uniq_cnt.items()]
    competitor_uniq_cnt_lst = sorted(competitor_uniq_cnt_lst, key=lambda tup: (-tup[0], tup[1]))
    print(f'competitor_uniq_cnt_lst {competitor_uniq_cnt_lst}')
    return [name for cnt, name in competitor_uniq_cnt_lst[0:topNCompetitors]]


# test0
numCompetitors = 6
# numCompetitors = 7
topNCompetitors = 2
competitors = ['newshop', 'shopnow', 'afshion', 'fashionbeats', 'mymarket', 'tcellular']
# competitors = ['newshop', 'shopnow', 'afshion', 'fashionbeats', 'mymarket', 'tcellular', 'fungame']
numReviews = 6
# numReviews = 8
reviews = [
    'newshop is providing new service to the city, everyone should use newshop',
    'best service by newshop',
    'fashionbeats has great service in the city',
    'I am proud to have fashionbeats',
    'mymarket has awesome services',
    'Thanks Newshop for the quick delivery',
    # 'MHW is a fungame',
    # 'LOL is also a fungame'
]
# expect return ['fashionbeats', 'newshop']
print(findTopNCompetitors(numCompetitors, topNCompetitors, competitors, numReviews, reviews))

