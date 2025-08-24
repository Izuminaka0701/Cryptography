# from Crypto.Util.number import *
# import gmpy2

# # Dữ liệu đề cho
# N = 14905562257842714057932724129575002825405393502650869767115942606408600343380327866258982402447992564988466588305174271674657844352454543958847568190372446723549627752274442789184236490768272313187410077124234699854724907039770193680822495470532218905083459730998003622926152590597710213127952141056029516116785229504645179830037937222022291571738973603920664929150436463632305664687903244972880062028301085749434688159905768052041207513149370212313943117665914802379158613359049957688563885391972151218676545972118494969247440489763431359679770422939441710783575668679693678435669541781490217731619224470152467768073

# e1 = 12886657667389660800780796462970504910193928992888518978200029826975978624718627799215564700096007849924866627154987365059524315097631111242449314835868137
# e2 = 12110586673991788415780355139635579057920926864887110308343229256046868242179445444897790171351302575188607117081580121488253540215781625598048021161675697

# c1 = 14010729418703228234352465883041270611113735889838753433295478495763409056136734155612156934673988344882629541204985909650433819205298939877837314145082403528055884752079219150739849992921393509593620449489882380176216648401057401569934043087087362272303101549800941212057354903559653373299153430753882035233354304783275982332995766778499425529570008008029401325668301144188970480975565215953953985078281395545902102245755862663621187438677596628109967066418993851632543137353041712721919291521767262678140115188735994447949166616101182806820741928292882642234238450207472914232596747755261325098225968268926580993051
# c2 = 14386997138637978860748278986945098648507142864584111124202580365103793165811666987664851210230009375267398957979494066880296418013345006977654742303441030008490816239306394492168516278328851513359596253775965916326353050138738183351643338294802012193721879700283088378587949921991198231956871429805847767716137817313612304833733918657887480468724409753522369325138502059408241232155633806496752350562284794715321835226991147547651155287812485862794935695241612676255374480132722940682140395725089329445356434489384831036205387293760789976615210310436732813848937666608611803196199865435145094486231635966885932646519

# # Ý tưởng: tìm e-th root mod N
# def modular_root(c, e, N):
#     try:
#         return int(gmpy2.iroot(c, e)[0])
#     except:
#         return None

# # Tính thử căn bậc e1, e2
# A = gmpy2.iroot(c1, e1)[0]  # ~ 2p + 3q
# B = gmpy2.iroot(c2, e2)[0]  # ~ 5p + 7q

# print("A ≈", A)
# print("B ≈", B)

# # Giải hệ 2 phương trình tuyến tính:
# # 2p + 3q = A
# # 5p + 7q = B
# # Dùng định thức
# det = 2*7 - 3*5
# p = (A*7 - B*3)//det
# q = (B*2 - A*5)//det

# print("p =", p)
# print("q =", q)

# # Kiểm chứng
# print("Check p*q == N ?", p*q == N)


# Modular_Binomials_bruteforce.py
# Usage: python3 Modular_Binomials_bruteforce.py
# Adjust max_k and max_l if needed.

# import sys
# from math import gcd
# from time import time

# # --- given constants (paste your values here) ---
# N = 14905562257842714057932724129575002825405393502650869767115942606408600343380327866258982402447992564988466588305174271674657844352454543958847568190372446723549627752274442789184236490768272313187410077124234699854724907039770193680822495470532218905083459730998003622926152590597710213127952141056029516116785229504645179830037937222022291571738973603920664929150436463632305664687903244972880062028301085749434688159905768052041207513149370212313943117665914802379158613359049957688563885391972151218676545972118494969247440489763431359679770422939441710783575668679693678435669541781490217731619224470152467768073

# e1 = 12886657667389660800780796462970504910193928992888518978200029826975978624718627799215564700096007849924866627154987365059524315097631111242449314835868137
# e2 = 12110586673991788415780355139635579057920926864887110308343229256046868242179445444897790171351302575188607117081580121488253540215781625598048021161675697

# c1 = 14010729418703228234352465883041270611113735889838753433295478495763409056136734155612156934673988344882629541204985909650433819205298939877837314145082403528055884752079219150739849992921393509593620449489882380176216648401057401569934043087087362272303101549800941212057354903559653373299153430753882035233354304783275982332995766778499425529570008008029401325668301144188970480975565215953953985078281395545902102245755862663621187438677596628109967066418993851632543137353041712721919291521767262678140115188735994447949166616101182806820741928292882642234238450207472914232596747755261325098225968268926580993051
# c2 = 14386997138637978860748278986945098648507142864584111124202580365103793165811666987664851210230009375267398957979494066880296418013345006977654742303441030008490816239306394492168516278328851513359596253775965916326353050138738183351643338294802012193721879700283088378587949921991198231956871429805847767716137817313612304833733918657887480468724409753522369325138502059408241232155633806496752350562284794715321835226991147547651155287812485862794935695241612676255374480132722940682140395725089329445356434489384831036205387293760789976615210310436732813848937666608611803196199865435145094486231635966885932646519
# # -------------------------------------------------

# # Config: how far to try (increase if you want but runtime grows fast)
# max_k = 200
# max_l = 200

# def try_gcd_tricks(N, c1, c2, max_k=200, max_l=200, verbose=True):
#     start = time()

#     # Strategy A: gcd(pow(c1, k, N) - c2, N)
#     if verbose: print("Strategy A: gcd(c1^k - c2, N)")
#     for k in range(1, max_k+1):
#         x = pow(c1, k, N)
#         g = gcd(x - c2, N)
#         if g not in (1, N):
#             return (g, N//g, f"A k={k}", time()-start)

#         if k % 50 == 0 and verbose:
#             print(f"  tried k={k} ...")

#     # Strategy B: gcd(pow(c2, l, N) - c1, N)
#     if verbose: print("Strategy B: gcd(c2^l - c1, N)")
#     for l in range(1, max_l+1):
#         y = pow(c2, l, N)
#         g = gcd(y - c1, N)
#         if g not in (1, N):
#             return (g, N//g, f"B l={l}", time()-start)

#         if l % 50 == 0 and verbose:
#             print(f"  tried l={l} ...")

#     # Strategy C: gcd(pow(c1,k,N) - pow(c2,l,N), N)
#     if verbose: print("Strategy C: gcd(c1^k - c2^l, N) (nested loops)")
#     # nested loops: be careful with bounds
#     for k in range(1, max_k+1):
#         x = pow(c1, k, N)
#         # inner loop smaller to be practical
#         for l in range(1, max_l+1):
#             y = pow(c2, l, N)
#             g = gcd(x - y, N)
#             if g not in (1, N):
#                 return (g, N//g, f"C k={k}, l={l}", time()-start)
#         if k % 20 == 0 and verbose:
#             print(f"  nested tried k={k} ... elapsed {time()-start:.1f}s")

#     return (None, None, "not found in ranges", time()-start)


# if __name__ == "__main__":
#     print("Starting brute-force gcd tricks...")
#     factor1, factor2, info, elapsed = try_gcd_tricks(N, c1, c2, max_k=max_k, max_l=max_l, verbose=True)

#     if factor1:
#         p = int(min(factor1, factor2))
#         q = int(max(factor1, factor2))
#         print("\n=== FOUND FACTORS ===")
#         print("Method:", info)
#         print("p =", p)
#         print("q =", q)
#         print("Check p*q == N ->", p * q == N)
#         print("Elapsed: {:.2f} seconds".format(elapsed))
#     else:
#         print("\nNo factor found in the tested ranges.")
#         print("Tried max_k =", max_k, "max_l =", max_l)
#         print("Elapsed: {:.2f} seconds".format(elapsed))
#         print("Suggestion: increase max_k/max_l or try different heuristics.")

#!/usr/bin/env python3
# full_modular_solver.py
# Combines gcd-tricks and factorization (Pollard Rho/Brent + optional pyecm).
# Usage: python3 full_modular_solver.py

import sys, math, random, time
from math import gcd

# ---- Paste the problem constants here ----
N = 14905562257842714057932724129575002825405393502650869767115942606408600343380327866258982402447992564988466588305174271674657844352454543958847568190372446723549627752274442789184236490768272313187410077124234699854724907039770193680822495470532218905083459730998003622926152590597710213127952141056029516116785229504645179830037937222022291571738973603920664929150436463632305664687903244972880062028301085749434688159905768052041207513149370212313943117665914802379158613359049957688563885391972151218676545972118494969247440489763431359679770422939441710783575668679693678435669541781490217731619224470152467768073

e1 = 12886657667389660800780796462970504910193928992888518978200029826975978624718627799215564700096007849924866627154987365059524315097631111242449314835868137
e2 = 12110586673991788415780355139635579057920926864887110308343229256046868242179445444897790171351302575188607117081580121488253540215781625598048021161675697

c1 = 14010729418703228234352465883041270611113735889838753433295478495763409056136734155612156934673988344882629541204985909650433819205298939877837314145082403528055884752079219150739849992921393509593620449489882380176216648401057401569934043087087362272303101549800941212057354903559653373299153430753882035233354304783275982332995766778499425529570008008029401325668301144188970480975565215953953985078281395545902102245755862663621187438677596628109967066418993851632543137353041712721919291521767262678140115188735994447949166616101182806820741928292882642234238450207472914232596747755261325098225968268926580993051
c2 = 14386997138637978860748278986945098648507142864584111124202580365103793165811666987664851210230009375267398957979494066880296418013345006977654742303441030008490816239306394492168516278328851513359596253775965916326353050138738183351643338294802012193721879700283088378587949921991198231956871429805847767716137817313612304833733918657887480468724409753522369325138502059408241232155633806496752350562284794715321835226991147547651155287812485862794935695241612676255374480132722940682140395725089329445356434489384831036205387293760789976615210310436732813848937666608611803196199865435145094486231635966885932646519
# ------------------------------------------

# ========== Utilities ==========
def is_probable_prime(n, rounds=8):
    if n < 2: return False
    small_primes = [2,3,5,7,11,13,17,19,23,29]
    for p in small_primes:
        if n % p == 0:
            return n == p
    d = n-1
    s = 0
    while d % 2 == 0:
        s += 1; d //= 2
    for _ in range(rounds):
        a = random.randrange(2, n-1)
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            continue
        for __ in range(s-1):
            x = (x*x) % n
            if x == n-1:
                break
        else:
            return False
    return True

# Pollard Rho (Brent)
def pollards_rho_brent(n, max_iter=100000):
    if n % 2 == 0:
        return 2
    if is_probable_prime(n):
        return n
    while True:
        y = random.randrange(2, n-1)
        c = random.randrange(1, n-1)
        m = random.randrange(1, n-1)
        g = 1
        r = 1
        q = 1
        x = y
        while g == 1:
            x = y
            for _ in range(r):
                y = (y*y + c) % n
            k = 0
            while k < r and g == 1:
                ys = y
                for _ in range(min(m, r-k)):
                    y = (y*y + c) % n
                    q = (q * abs(x - y)) % n
                g = math.gcd(q, n)
                k += m
            r <<= 1
        if g == n:
            g = 1
            while g == 1:
                ys = (ys*ys + c) % n
                g = math.gcd(abs(x-ys), n)
        if g != n:
            return g

# Try factorization using Pollard Rho several times
def try_factor_rho(n, trials=6):
    if n == 1: return None
    if is_probable_prime(n):
        return n
    for t in range(trials):
        f = pollards_rho_brent(n)
        if f is None or f == 1 or f == n:
            continue
        return f
    return None

# Optional: attempt using pyecm if installed
def try_pyecm(n, timeout=30):
    try:
        import pyecm
    except Exception as e:
        print("  pyecm not installed; skipping ECM.")
        return None
    print("  running pyecm.ecm... (may take a while)")
    start = time.time()
    for factor in pyecm.factors(n, False, False, lambda: time.time()-start > timeout):
        return factor
    return None

# ========== Algebraic gcd-tricks ==========
def gcd_tricks(N, c1, c2, max_k=400, max_l=400, verbose=True):
    # tries multiple patterns; returns a factor if found
    start = time.time()
    if verbose: print("[*] Trying gcd-tricks (A)...")
    # Strategy 1: gcd(c1^k - c2, N)
    for k in range(1, max_k+1):
        g = math.gcd(pow(c1, k, N) - c2, N)
        if 1 < g < N:
            return g, f"gcd(c1^{k} - c2, N)"
        if k % 100 == 0 and verbose:
            print(f"  tried k={k}")
    # Strategy 2: gcd(c2^l - c1, N)
    if verbose: print("[*] Trying gcd-tricks (B)...")
    for l in range(1, max_l+1):
        g = math.gcd(pow(c2, l, N) - c1, N)
        if 1 < g < N:
            return g, f"gcd(c2^{l} - c1, N)"
        if l % 100 == 0 and verbose:
            print(f"  tried l={l}")
    # Strategy 3: gcd(c1^k - c2^l, N) nested but bounded
    if verbose: print("[*] Trying gcd-tricks (C) nested loops...")
    for k in range(1, min(200, max_k)+1):
        x = pow(c1, k, N)
        for l in range(1, min(200, max_l)+1):
            y = pow(c2, l, N)
            g = math.gcd(x - y, N)
            if 1 < g < N:
                return g, f"gcd(c1^{k} - c2^{l}, N)"
    # no luck
    return None, "no gcd-trick found in ranges"

# ========== Solve after factoring ==========
def solve_after_factor(p, q):
    print(f"[+] Got factors p={p} q={q}")
    phi = (p-1)*(q-1)
    try:
        d1 = pow(e1, -1, phi)
        d2 = pow(e2, -1, phi)
    except ValueError:
        print("  can't invert e1 or e2 mod phi (no inverse).")
        return False
    A = pow(c1, d1, N)
    B = pow(c2, d2, N)
    print("  Recovered A (2p+3q) =", A)
    print("  Recovered B (5p+7q) =", B)
    # Solve linear system:
    # 2p + 3q = A
    # 5p + 7q = B
    det = 2*7 - 3*5
    p_calc = (A*7 - B*3) // det
    q_calc = (B*2 - A*5) // det
    print("  Solved p_calc =", p_calc)
    print("  Solved q_calc =", q_calc)
    print("  Check p_calc*q_calc == N ?", p_calc * q_calc == N)
    return p_calc * q_calc == N

# ========== Main flow ==========
def main():
    print("=== full_modular_solver ===")
    t0 = time.time()

    # First: try gcd-based algebraic tricks
    f, info = gcd_tricks(N, c1, c2, max_k=400, max_l=400, verbose=True)
    if f:
        print(f"[+] gcd trick found factor: {f} via {info}")
        other = N // f
        if solve_after_factor(min(f, other), max(f, other)):
            print("[+] Success via gcd-trick!")
            return
        else:
            print("  but solving A/B didn't verify — continuing to factor N directly.")

    # Second: try Pollard Rho / Brent
    print("[*] Trying Pollard-Brent Rho factorization...")
    f = try_factor_rho(N, trials=10)
    if f and f not in (1, N):
        other = N // f
        print(f"[+] Pollard found factor: {f}")
        if solve_after_factor(min(f, other), max(f, other)):
            print("[+] Success via Pollard Rho!")
            return
    else:
        print("  Pollard Rho failed to find a nontrivial factor quickly.")

    # Third: try pyecm if available (recommended for CTF RSA-sized composites)
    print("[*] Trying pyecm (ECM) if installed. Install via: pip install pyecm")
    f = try_pyecm(N, timeout=45)
    if f and f not in (1, N):
        other = N // f
        print(f"[+] pyecm found factor: {f}")
        if solve_after_factor(min(f, other), max(f, other)):
            print("[+] Success via ECM!")
            return
    else:
        print("  pyecm either not installed, timed out, or didn't find a factor.")

    # Last: full fallback messaging
    print("\n[-] All quick methods exhausted.")
    print("Suggestions:")
    print("  - Increase gcd-trick ranges (max_k,max_l) if you suspect small exponent relations.")
    print("  - Run this on a beefy machine and install pyecm (ECM).")
    print("  - If you want I can produce a pure ECM runner or integrate msieve/gmp-ecm (but those require native installs).")
    print("Elapsed: {:.2f}s".format(time.time() - t0))

if __name__ == '__main__':
    main()

