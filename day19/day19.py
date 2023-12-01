def main():

    # workflow: [(rule, ), ....]
    workflow = dict()
    work_parts = []

    def is_accepted(part, wf):
        if wf == 'A':
            return True
        if wf == 'R':
            return False

        current_workflow = workflow[wf]
        for ff in current_workflow:
            gf = ff.split(':')
            if len(gf) == 1:
                return is_accepted(part, gf[0])

            condition = gf[0]
            next_workflow = gf[1]
            lt = condition.split('<')
            gt = condition.split('>')
            if len(lt) > 1:
                if part[lt[0]] < int(lt[1]):
                    return is_accepted(part, next_workflow)
            if len(gt) > 1:
                if part[gt[0]] > int(gt[1]):
                    return is_accepted(part, next_workflow)


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

    ss_1 = 0
    for pa in work_parts:
        if is_accepted(pa, 'in'):
            for zzz in pa.values():
                ss_1 += zzz
    print(ss_1)


if __name__ == '__main__':
    main()
