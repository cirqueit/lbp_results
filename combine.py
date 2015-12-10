import json

abstract_faces = [
        'tress-photo.gif',
        'henry.gif',
        'herbie-hancock.gif',
        'cards-perp-sml.gif',
        'torrance.gif',
        'u2-cover.gif',
        'our-cards.gif',
        'aeon1a.gif',
        'board.gif',
        ]


fnames = [
                {'name': 'ocv haar', 'dic': {}, 'src': 'frontal_face_haar.json'},
                {'name': 'ocv alt', 'dic': {}, 'src': 'frontal_face_haar_alt.json'},
                {'name': 'ocv alt2','dic': {}, 'src': 'frontal_face_haar_alt2.json'},
                {'name': 'ocv lbp',  'dic': {}, 'src': 'frontal_face.json'},
                # {'name': 'lbpr2b 10k',  'dic': {}, 'src': 'boot2_10.json'},
                # {'name': 'lbpr2 20k 16',  'dic': {}, 'src': '20k_2_8_16.json'},
                # {'name': 'lbpr2 20k 20',  'dic': {}, 'src': '20k_2_8_20.json'},
                # {'name': 'lbpr2 20k 24',  'dic': {}, 'src': '20k_2_8_24.json'},
                # {'name': 'lbprb2 20k 24',  'dic': {}, 'src': '20k_2_10_24.json'},
                # {'name': 'lbpr 40k 24',  'dic': {}, 'src': '40k_r_8_24_20.json'},
                # {'name': 'lbp 40k 24',  'dic': {}, 'src': '40k_d_8_24_20.json'},
                # {'name': 'lbpr2 40k',  'dic': {}, 'src': '40k_2_8_24_20.json'},
                # {'name': 'lbpr2 40kx',  'dic': {}, 'src': '40k_2_8_24_24.json'},
                # {'name': 'lbpr 40kx',  'dic': {}, 'src': '40k_r_8_24_24.json'},
                # {'name': 'lbpr2 20kx',  'dic': {}, 'src': '20k_2_8_24_24.json'},
                # {'name': 'lbpr 20kx',  'dic': {}, 'src': '20k_r_8_24_24.json'},
                # {'name': 'lbpr2 100k',  'dic': {}, 'src': '100k_2_8_24_20.json'},
                # {'name': 'lbpr 100k',  'dic': {}, 'src': '100k_r_8_24_20.json'},
                # {'name': 'lbp 100k',  'dic': {}, 'src': '100k_d_8_24_20.json'},
                # {'name': 'lbprb 100kx',  'dic': {}, 'src': '100k_r_8_24_24.json'},
                # {'name': 'lbp2 100k9 96',  'dic': {}, 'src': '100k9_2_10_48_20_n10.json'},
                # {'name': 'lbp2 100k9 64',  'dic': {}, 'src': '100k9_2_10_64_20_n10.json'},
                # {'name': 'lbp2 200k 48',  'dic': {}, 'src': 'w20_h99999_m3_p200000_n20000_s48_f16_r2.json'},
                # {'name': 'lbp2 200k xx',  'dic': {}, 'src': 'w20_h99999_m3_p200000_n20000_f16_r2.json'},
                # {'name': 'lbp r2',  'dic': {}, 'src': 'w20_h99999_m3_p200000_n20000_f16_r2_s76.json'},
                # {'name': 'lbp r2b+',  'dic': {}, 'src': 'w24_h999_m3_p200000_n10000_f16_r2_s14.json'},
                # {'name': 'lbp r28',  'dic': {}, 'src': 'w20_h999_m3_p200000_n10000_f8_r2_s25.json'},
                # {'name': 'lbp r28+',  'dic': {}, 'src': 'w20_h999_m3_p200000_n10000_f8_r2_s28.json'},
                # {'name': 'lbp r2b',  'dic': {}, 'src': 'w24_h999_m3_p200000_n10000_f16_r2_s13.json'},
                # {'name': 'lbp r2',  'dic': {}, 'src': 'w20_h999_m3_p200000_n10000_f16_r2_s13.json'},
                {'name': 'lbp r2 16',  'dic': {}, 'src': 'w20_h999_m3_p200000_n10000_f16_r2_s16.json'},
                {'name': 'lbp',  'dic': {}, 'src': 'w20_h9995_m3_p100000_n100000_s9.json'},
                {'name': 'lbp r',  'dic': {}, 'src': 'w20_h9995_m3_p100000_n100000_r_s9.json'},
                {'name': 'lbp r2',  'dic': {}, 'src': 'w20_h9995_m3_p100000_n100000_r2_s9.json'},
                {'name': 'lbp9',  'dic': {}, 'src': 'w20_h9999_m3_p100000_n100000_s9.json'},
                {'name': 'lbp9 r',  'dic': {}, 'src': 'w20_h9999_m3_p100000_n100000_r_s9.json'},
                {'name': 'lbp9 r2',  'dic': {}, 'src': 'w20_h9999_m3_p100000_n100000_r2_s9.json'},
                {'name': 'lbp99',  'dic': {}, 'src': 'w20_h99999_m3_p100000_n100000_s9.json'},
                {'name': 'lbp99 r',  'dic': {}, 'src': 'w20_h99999_m3_p100000_n100000_r_s9.json'},
                {'name': 'lbp99 r2',  'dic': {}, 'src': 'w20_h99999_m3_p100000_n100000_r2_s9.json'},
                # {'name': 'lbp r29',  'dic': {}, 'src': 'w20_h9999_m3_p200000_n10000_f16_r2_s28.json'},
                # {'name': 'lbp r1',  'dic': {}, 'src': 'w20_h99995_m3_p200000_n10000_f16_r_s15.json'},
                # {'name': 'lbp r1+6',  'dic': {}, 'src': 'w20_h99995_m3_p200000_n10000_f16_r_s21.json'},
                {'name': 'l10 r2',  'dic': {}, 'src': 'w20_h999_m3_p50000_n50000_f10_r2.json'},
                {'name': 'l10 r',  'dic': {}, 'src': 'w20_h999_m3_p50000_n50000_f10_r.json'},
                {'name': 'l10',  'dic': {}, 'src': 'w20_h999_m3_p50000_n50000_f10.json'},
                {'name': 'l8 r2',  'dic': {}, 'src': 'w20_h999_m3_p50000_n50000_f8_r2.json'},
                {'name': 'l8 r',  'dic': {}, 'src': 'w20_h999_m3_p50000_n50000_f8_r.json'},
                {'name': 'l8',  'dic': {}, 'src': 'w20_h999_m3_p50000_n50000_f8.json'},
                {'name': 'pl10 r2',  'dic': {}, 'src': 'w20_h9999_m3_p50000_n50000_f10_r2.json'},
                {'name': 'pl10 r',  'dic': {}, 'src': 'w20_h9999_m3_p50000_n50000_f10_r.json'},
                {'name': 'pl10',  'dic': {}, 'src': 'w20_h9999_m3_p50000_n50000_f10.json'},
                {'name': 'pl8 r2',  'dic': {}, 'src': 'w20_h9999_m3_p50000_n50000_f8_r2.json'},
                {'name': 'pl8 r',  'dic': {}, 'src': 'w20_h9999_m3_p50000_n50000_f8_r.json'},
                {'name': 'pl8',  'dic': {}, 'src': 'w20_h9999_m3_p50000_n50000_f8.json'},
                {'name': 'l8 r2 s32',  'dic': {}, 'src': 'w20_h999_m3_p50000_n50000_f8_r2_s32.json'},
                {'name': 'l10 r2 s25',  'dic': {}, 'src': 'w20_h999_m3_p50000_n50000_f10_r2_s25.json'},
        ]

def combine():
    for i, d in enumerate(fnames):
        with open(d['src'], 'r') as f:
            fnames[i]['dic'] = json.load(f)

    base = {}
    with open('ground.json', 'r') as f:
        base = json.load(f)

    for i in range(len(base)):
        iname = base[i]['name']
        for f in fnames:
            cascade = f['name']
            for img in f['dic'].keys():
                if img == iname:
                    base[i][cascade] = f['dic'][img]

    with open('combined.json', 'w') as f:
        json.dump(base, f)
            
def compare_rect(ground, test):
    fp = 0
    tp = 0

    positive = len(ground)
    hits = [0 for i in range(positive)]

    for t in test:
        is_hit = False
        for i in range(positive):
            if overlap(ground[i], t):
                hits[i] = hits[i] + 1
                is_hit = True
        if not is_hit:
            fp = fp + 1

    for i in range(positive):
        if hits[i] > 0:
            tp = tp + 1
        if hits[i] > 1:
            fp = fp + 1

    return tp, fp

def overlap(ground, test):
    gx = ground[0]
    gy = ground[1]
    gw = ground[2]
    gh = ground[3]

    tx = test[0]
    ty = test[1]
    tw = test[2]
    th = test[3]

    left = max(gx, tx)
    right = min(gx+gw, tx+tw)

    top = max(gy, ty)
    bottom = min(gy+gh, ty+th)

    w = right - left
    h = bottom - top

    if w < 0 or h < 0:
        return False

    oarea = w * h
    garea = gw * gh

    if (oarea * 1.0 / garea) > 0.40:
        return True
    else:
        return False

def compare():
    
    combined = {}

    with open('combined.json', 'r') as f:
        combined = json.load(f)

    for i in range(len(combined)):
        ground = combined[i]['ground']
        cascades = [key for key in combined[i].keys() if key != 'name' and key != 'ground']
        for cascade in cascades:
            for v in range(len(combined[i][cascade])):
                test = combined[i][cascade][v]['faces']
                tp, fp =  compare_rect(ground, test)
                combined[i][cascade][v]['tp'] = tp
                combined[i][cascade][v]['fp'] = fp

    rates = []
    total_faces = 0
    select_faces = 0
    cascades = []
    for i in range(len(combined)):
        total_faces = total_faces + len(combined[i]['ground'])
        if combined[i]['name'] not in abstract_faces:
            select_faces = select_faces + len(combined[i]['ground'])
        cascades = [key for key in combined[i].keys() if key != 'name' and key != 'ground']


    for mn in range(7):
        for scale in [1.1, 1.3]:
            for cascade in cascades:
                total_fp = 0
                total_tp = 0
                for i in range(len(combined)):
                    for v in range(len(combined[i][cascade])):
                        if combined[i][cascade][v]['min_neighbors'] == mn:
                            if combined[i][cascade][v]['scale'] == scale:
                                total_tp = total_tp + combined[i][cascade][v]['tp']
                                total_fp = total_fp + combined[i][cascade][v]['fp']
                select_fp = 0
                select_tp = 0
                for i in range(len(combined)):
                    if combined[i]['name'] not in abstract_faces:
                        for v in range(len(combined[i][cascade])):
                            if combined[i][cascade][v]['min_neighbors'] == mn:
                                if combined[i][cascade][v]['scale'] == scale:
                                    select_tp = select_tp + combined[i][cascade][v]['tp']
                                    select_fp = select_fp + combined[i][cascade][v]['fp']
                rates.append({'min_neighbors': mn, 'scale': scale, 'cascade': cascade,
                    'tp': total_tp, 'fp': total_fp, 'tpr': total_tp * 1.0 / total_faces, 'fpr': total_fp * 1.0 / total_faces,
                    'stp': select_tp, 'sfp': select_fp, 'stpr': select_tp * 1.0 / select_faces, 'sfpr': select_fp * 1.0 / select_faces,
                    })


    with open('compared.json', 'w') as f:
        json.dump(combined, f)

    with open('rates.json', 'w') as f:
        json.dump(rates, f)

if __name__ == "__main__":

    combine()
    compare()
