import re


def prepare_base_bouquet(designs, flower, flowers):
    flowers.setdefault(flower, 0)
    flowers[flower] += 1
    for des in designs['designs']:
        for flow in des['req_flowers']:
            specie = flow + des['size']
            if specie == flower and des['act_flowers'][flow] < des['req_flowers'][flow] and flowers[flower] > 0:
                des['act_flowers'][flow] += 1
                flowers[flower] -= 1

    for des in designs['designs']:
        if (sum(des['act_flowers'].values()) < des['tot_number']
            and sum([des['act_flowers'][k] for k in des['req_flowers']]) == sum(des['req_flowers'].values())
                and flowers[flower] > 0 and flower not in [k + des['size'] for k in des['req_flowers'].keys()]):

            fl = flower
            if fl .endswith(des['size']):
                fl = fl[0]

            des['act_flowers'].setdefault(fl, 0)
            des['act_flowers'][fl] += 1
            flowers[flower] -= 1

        if sum(des['act_flowers'].values()) == des['tot_number']:
            if not des['bouquet']:
                des['bouquet'] = des['name']\
                                 + des['size']\
                                 + ''.join([str(des['act_flowers'][k]) + k for k in des['act_flowers']])
                print(f"{des['bouquet']}")


def prepare_bouquet_dict(data):
    design = dict()
    design['design'] = data
    design['bouquet'] = None
    design['tot_number'] = int(data[-2:])
    design['name'] = data[0]
    design['size'] = data[1]
    design_parsed = re.split(r'([a-z]+)', data[2:])
    design['req_flowers'] = dict(zip(design_parsed[1:-1:2], map(int, design_parsed[0:-1:2])))
    design['act_flowers'] = dict(zip(design_parsed[1:-1:2], [0] * len(design_parsed[1:-1:2])))

    return design


def main():
    designs = {'designs': []}
    flowers = {}
    while True:
        try:
            data = input()
            if len(data) > 2:
                designs['designs'].append(prepare_bouquet_dict(data))

            elif len(data) == 2:
                prepare_base_bouquet(designs, data, flowers)

        except EOFError:
            break


if __name__ == '__main__':
    main()
