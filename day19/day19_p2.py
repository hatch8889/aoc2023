def main():
    workflow = dict()
    work_parts = []

    def is_accepted(wwwf, xr, mr, ar, sr):
        ppp = len(list(xr)) * len(list(mr)) * len(list(ar)) * len(list(sr))
        if ppp == 0:
            return 0

        if wwwf == 'A':
            return ppp

        if wwwf == 'R':
            return 0

        current_workflow = workflow[wwwf]
        total = 0

        xr2 = list(xr)
        mr2 = list(mr)
        ar2 = list(ar)
        sr2 = list(sr)

        for ff in current_workflow:
            gf = ff.split(':')
            if len(gf) == 1:
                total += is_accepted(gf[0], xr2, mr2, ar2, sr2)
                break

            condition = gf[0]
            next_workflow = gf[1]
            lt = condition.split('<')
            gt = condition.split('>')

            xr3 = list(xr2)
            mr3 = list(mr2)
            ar3 = list(ar2)
            sr3 = list(sr2)

            if len(lt) > 1:
                if lt[0] == 'x':
                    xr3 = list(filter(lambda s: s < int(lt[1]), xr2))
                    xr2 = list(filter(lambda s: s >= int(lt[1]), xr2))
                elif lt[0] == 'm':
                    mr3 = list(filter(lambda s: s < int(lt[1]), mr2))
                    mr2 = list(filter(lambda s: s >= int(lt[1]), mr2))
                elif lt[0] == 'a':
                    ar3 = list(filter(lambda s: s < int(lt[1]), ar2))
                    ar2 = list(filter(lambda s: s >= int(lt[1]), ar2))
                elif lt[0] == 's':
                    sr3 = list(filter(lambda s: s < int(lt[1]), sr2))
                    sr2 = list(filter(lambda s: s >= int(lt[1]), sr2))
            elif len(gt) > 1:
                if gt[0] == 'x':
                    xr3 = list(filter(lambda s: s > int(gt[1]), xr2))
                    xr2 = list(filter(lambda s: s <= int(gt[1]), xr2))
                elif gt[0] == 'm':
                    mr3 = list(filter(lambda s: s > int(gt[1]), mr2))
                    mr2 = list(filter(lambda s: s <= int(gt[1]), mr2))
                elif gt[0] == 'a':
                    ar3 = list(filter(lambda s: s > int(gt[1]), ar2))
                    ar2 = list(filter(lambda s: s <= int(gt[1]), ar2))
                elif gt[0] == 's':
                    sr3 = list(filter(lambda s: s > int(gt[1]), sr2))
                    sr2 = list(filter(lambda s: s <= int(gt[1]), sr2))

            total += is_accepted(next_workflow, xr3, mr3, ar3, sr3)

        return total

    with open('data.txt') as data:
        wf = True
        lines = data.read().splitlines()
        for line in lines:
            if line == '':
                wf = False
                continue

            if wf:
                parts = line.split('{')
                wf_name = parts[0]
                s_rules = parts[1].strip('}').split(',')
                workflow[wf_name] = s_rules
                continue
            elif line.startswith('{'):
                pps = dict()
                for p in line.strip('{}').split(','):
                    ee = p.split('=')
                    pps[ee[0]] = int(ee[1])
                work_parts.append(pps)

    ss_2 = is_accepted('in', range(1, 4001), range(1, 4001), range(1, 4001), range(1, 4001))
    print(ss_2)


if __name__ == '__main__':
    main()
