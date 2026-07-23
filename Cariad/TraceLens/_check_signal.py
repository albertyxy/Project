# -*- coding: utf-8 -*-
from asammdf import MDF
import numpy as np

file_path = r"data\Gen5_2026-06-30_20-39_Y653_RC1__0067.MF4"

with MDF(file_path) as mdf:
    # 找 _m_values._0_ 到 _4_ 的 TTC 通道
    ttc = {}
    for i in range(5):
        candidates = [k for k in mdf.channels_db
                      if f"_m_values._{i}_._m_objectData._m_ttc._m_value" in k
                      and "MainProcSfBase" in k]
        if candidates:
            ttc[i] = candidates[0]

    if not ttc:
        print("未找到 TTC 通道")
    else:
        # 提取所有
        data = {}
        for i, name in ttc.items():
            s = mdf.get(name)
            data[i] = (s.timestamps.astype(np.float64), s.samples.astype(np.float64))
            print(f"槽位 {i}: {name[-60:]}")

        print(f"\n{'t(s)':<12}", end="")
        for i in sorted(data):
            print(f"{'TTC_'+str(i):<16}", end="")
        print("排序正确?")

        # 在 90-110s 区间均匀采样 5 个时间点
        t0 = data[0][0]
        mask = (t0 >= 90) & (t0 <= 100)
        t = t0[mask]
        step = max(1, len(t) // 5)
        for j in range(0, len(t), step):
            if j >= 5 * step:
                break
            ts = t[j]
            print(f"{ts:<12.4f}", end="")
            vals = []
            for i in sorted(data):
                t_arr, s_arr = data[i]
                idx = np.argmin(np.abs(t_arr - ts))
                v = s_arr[idx]
                if np.isnan(v) or v > 1e30:
                    v_str = "INVALID"
                else:
                    v_str = f"{v:<14.3f}"
                print(f"{v_str:<16}", end="")
                if i > 0 and not np.isnan(v) and v < 1e30:
                    vals.append(v)
            # 检查是否升序
            ordered = all(vals[j] <= vals[j+1] for j in range(len(vals)-1)) if len(vals) > 1 else True
            print("OK" if ordered else "乱序!")
