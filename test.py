import restricted_main

formulae = [
    '[] <> (l2_1_2_0 && <> l4_1_4_0)',
    '<> l2_1_1_0 && <> l4_1_1_0 && l1_1_1_0 U l4_1_1_0',
    '<> (l4_1_2_1 && l3_1_1_0 && !l4_2_1) && <> l5_1_2_1 && [] !l2_1_1',
    '<> (l3_1_2_1 && <> l4_1_2_1)',
    '[] <> (l3_1_2_1 && <> l4_1_2_1) && <> l5_2_1_0',
    '[] <> (l4_1_2_1 && <> l3_1_2_1) && <> l4_2_1_0 && ! l3_1_2 U l4_2_1_0',
    '(l1_1_2_0 && !l2_1_1) U (l2_1_2_0 && ! l1_2_1 && !l1_1_1)',
    # '<> l2_1_1_0 && <> l4_2_1_0 && []!(l2_1_1 && l4_2_1)',
    '<> (l2_1_1_0 ||  ! l3_1_1)',
    '(l1_1_2_0) U (l2_1_2_0 )',
    '[]<> l2_1_12_0 && []<> l3_1_6_0 && [] <> l4_1_6_0 && (!l4_1_1 U (l5_1_1_0 && l6_1_1_0))',
    '[] <> (l4_1_1_1 && <> l3_1_1_1) && []! l2_1_1',
    '<> l2_1_1_1 && [] <> (l4_1_1_1  && l3_1_1_0)',
    '[] <> (l4_1_2_1 && <> l3_1_2_1) && []! l5_1_2 && <> [] l6_2_2_0',
    '[] <> (l4_1_3_1 && <> l3_1_3_1) && <> [] l2_2_4_0',
    '<> (l4_1_1_0 || l5_1_1_0)']


for formula in formulae:
    restricted_main.ltl_mrta(formula)
