# Week 3: Revised Simplex and Duality Start (Lectures 11-15)

Coverage: revised simplex ($B^{-1}$, $\pi = c_B B^{-1}$, deviations $\bar{c}_j = c_j - \pi P_j$), case studies (transport/diet formulation, convexity, quadrant LPPs, two-phase feasibility, Big-M multiple optima), Module-1 quiz bank, symmetric primal-dual construction. Sources: Notes Module 1, Notes Module 2 Sec. 1, lec11-lec15 transcripts.

## Questions

**Q1.** In the revised simplex method, which quantities are carried from iteration to iteration instead of the full tableau?

  a) Only the objective value $z$ and the RHS $b$
  b) The basis inverse $B^{-1}$, the current RHS $\bar{b} = B^{-1}b$, the entering column $\bar{P}_k = B^{-1}P_k$, and the simplex multipliers $\pi = c_B B^{-1}$
  c) All $c_j - z_j$ entries for every variable including artificials kept forever
  d) Only the original matrix $A$ and the original cost vector $c$

**Q2.** In the optimal tableau of a Max LPP, a non-basic variable has deviation (reduced cost) $\bar{c}_j = 0$. This signals:

  a) unbounded solution
  b) infeasible solution
  c) multiple (alternate) optimal solutions
  d) degenerate but unique solution

*Source: Lecture 14 quiz*

**Q3.** During simplex iterations for a Max problem, the entering variable $x_k$ has every pivot-column entry $\le 0$, so the minimum-ratio test fails. This means:

  a) the problem has multiple optima
  b) the problem is infeasible
  c) the problem is unbounded
  d) the current basis is optimal and unique

*Source: Lecture 14 quiz*

**Q4.** For the running Big-M example of Lecture 11 (Max $3x_1 - x_2 - x_3 - Mx_6 - Mx_7$, final basis $\{x_1, x_2, x_3\} = (4,1,9)$), the final simplex multipliers $\pi = c_B B^{-1}$ equal:

  a) $(0, -M, -M)$
  b) $(0, -M, 2M-1)$
  c) $(0, -1, 1)$
  d) $(1/3, -1/3, 2/3)$

**Q5.** Primal: Max $z = 3x_1 + 4x_2$ s.t. $7x_1 - 2x_2 \ge 4$, $-3x_1 + x_2 \le 3$, $x_1, x_2 \ge 0$. After normalising to Max-with-$\le$ form, the symmetric dual is:

  a) Min $w = -4y_1 + 3y_2$ s.t. $-7y_1 - 3y_2 \ge 3$, $2y_1 + y_2 \ge 4$, $y_1, y_2 \ge 0$
  b) Max $w = -4y_1 + 3y_2$ s.t. $-7y_1 - 3y_2 \le 3$, $2y_1 + y_2 \le 4$, $y_1, y_2 \ge 0$
  c) Min $w = 4y_1 + 3y_2$ s.t. $7y_1 - 3y_2 \ge 3$, $-2y_1 + y_2 \ge 4$, $y_1, y_2 \ge 0$
  d) Min $w = 3y_1 + 4y_2$ s.t. $7y_1 - 2y_2 \ge -4$, $-3y_1 + y_2 \ge 3$, $y_1, y_2 \ge 0$

*Source: Lecture 15 homework*

**Q6.** Solve by revised simplex (track $B^{-1}$ and $\pi$ each iteration): Min $z = x_1 + 2x_2 + x_3$ s.t. $2x_1 + x_2 + x_3 \le 2$, $3x_1 + 4x_2 + 2x_3 \ge 16$, $x_1, x_2, x_3 \ge 0$. Report the LP status and, if feasible, the optimum.

*Source: Lecture 11 exercise*

**Q7.** Dog-feed diet problem (Lecture 12): Min $10x_1 + 20x_2$ s.t. $4x_1 + 5x_2 \ge 16$, $2x_1 + x_2 \ge 4$, $x_2 \ge 2x_1$, $x_1, x_2 \ge 0$. Find the optimal $(x_1, x_2)$ and minimum cost.

*Source: Lecture 12 exercise*

**Q8.** Solve by two-phase: Min $Z = 3x_1 + 2x_2 + x_3$ s.t. $x_1 + x_2 + x_3 = 4$, $2x_1 + 5x_2 - 2x_3 = 3$, $x \ge 0$. Report $(x_1, x_2, x_3)$ and $Z^*$.

*Source: Lecture 13 exercise*

**Q9.** State the two advantages of the revised simplex method emphasised in Lecture 11, and explain what the simplex multipliers $\pi$ will be used for in later modules.

**Q10.** State the six symmetric primal-dual construction rules, and use them to explain why the dual of the dual is the primal.

*Source: Lecture 15 homework (second part)*

## Answer key

| Q | Answer |
|---|---|
| 1 | (b) |
| 2 | (c) |
| 3 | (c) |
| 4 | (d) |
| 5 | (a) |
| 6 | Infeasible (Phase-1/Big-M ends with artificial $> 0$ in basis; max of $3x_1+4x_2+2x_3$ under row 1 is $8 < 16$) |
| 7 | $x_1 = 8/7$, $x_2 = 16/7$, $z^* = 400/7 \approx 57.14$ |
| 8 | $(11/4, 0, 5/4)$, $Z^* = 19/2$ |
| 9 | See solution: less memory/computation; $\pi$ solves dual + drives sensitivity |
| 10 | See solution: six rules; double transpose/direction swap restores primal |

## Worked solutions

**Q1. Given:** Revised simplex of Lec 11 on the $3 \times 3$ Big-M example. **Steps:** Full tableau recomputes every column; only $\bar{b}$, the entering $\bar{P}_k$, and $\pi$ (for $\bar{c}_j = c_j - \pi P_j$) are needed. $B^{-1}$ generates all of them. **Answer:** (b).

**Q2. Given:** Optimal Max tableau, non-basic $\bar{c}_j = 0$. **Steps:** Lecture 14 quiz Q9 / Lec-8 rule: zero deviation on a non-basic at optimum means that variable can enter without changing $z$; pivoting gives a second corner; convex combinations are all optimal. (Unbounded is ratio-test failure; infeasible is artificial $>0$ in basis.) **Answer:** (c).

**Q3. Given:** Positive $\bar{c}_k$ but no $p_{ik} > 0$. **Steps:** Lecture 14 quiz Q11 / Lec-9 rule: no leaving variable exists; the ray in direction $k$ stays feasible while $z \to \infty$. **Answer:** (c).

**Q4. Given:** Iteration table of Lec 11 Sec. 11.2. **Steps:** Iter 1: $c_B = (0,-M,-M)$, $\pi = (0,-M,-M)$; Iter 2: $c_B = (0,-M,-1)$, $\pi = (0,-M,2M-1)$; Iter 3: $c_B = (0,-1,-1)$, $\pi = (0,-1,1)$; Iter 4: $c_B = (3,-1,-1)$ times $B^{-1} = [[1/3,0,2/3],[2/3,1,4/3],[-5/3,-2,-7/3]]$ gives $(1/3,-1/3,2/3)$, and all $\bar{c} \le 0$. **Answer:** (d).

**Q5. Given:** Max problem with one $\ge$ row. **Steps:** Normalise Max to all-$\le$: multiply row 1 by $-1$: $-7x_1 + 2x_2 \le -4$; row 2 unchanged $-3x_1 + x_2 \le 3$. Apply six rules: one $y_i \ge 0$ per row; dual costs $= (-4, 3)$; dual RHS $= (3,4)$; matrix transposed; Max $\to$ Min; $\le \to \ge$. Dual: Min $-4y_1 + 3y_2$ s.t. $-7y_1 - 3y_2 \ge 3$, $2y_1 + y_2 \ge 4$, $y \ge 0$. Option (b) wrong direction; (c) forgot the $-1$ flip; (d) swaps $b$ and $c$. **Answer:** (a).

**Q6. Given:** Min $x_1+2x_2+x_3$ with rows $\le 2$ and $\ge 16$. **Steps:** Add slack $x_4$ in row 1; subtract surplus $x_5$ and add artificial $x_6$ in row 2; Big-M/revised simplex from $B = [P_4, P_6]$. Equivalently, feasibility needs $3x_1+4x_2+2x_3 \ge 16$ while $2x_1+x_2+x_3 \le 2$. Maximising $3x_1+4x_2+2x_3$ over row 1 alone gives vertices $(1,0,0)\to 3$, $(0,2,0)\to 8$, $(0,0,2)\to 4$, so max $= 8 < 16$. Hence Phase 1 ends with $x_6 > 0$ in basis. **Answer:** Infeasible.

**Q7. Given:** Diet data; simplified rows $4x_1+5x_2 = 16$ through $(0,16/5),(4,0)$; $2x_1+x_2 = 4$ through $(0,4),(2,0)$; $x_2 = 2x_1$ through $(1,2),(2,4)$; origin fails first two so feasible side is above. **Steps:** Corners: $A(0,4)$ from row 2 + $x_1 = 0$; $B(2/3,8/3)$ from rows 1-2 ($4x_1+5(4-2x_1) = 16 \Rightarrow x_1 = 2/3$); $C(8/7,16/7)$ from row 1 + $x_2 = 2x_1$ ($14x_1 = 16$). Costs $10x_1+20x_2$: $80$, $60$, $400/7 \approx 57.14$. **Answer:** $C = (8/7, 16/7)$, $z^* = 400/7$.

**Q8. Given:** Two equalities; add artificials $A_1, A_2$; Phase 1 Max $-A_1-A_2$. **Steps:** T1 deviations $(3,6,-1)$; enter $x_2$ (pivot 5) to basis $(A_1,x_2)$; deviations $(8/5,0,7/5)$; enter $x_3$ (pivot $7/5$) to basis $(x_3,x_2) = (17/7,11/7)$, deviations $(0,0,0,-1,-1)$, $W = 0$. Drop $A_1,A_2$. Phase 2 with costs $(3,2,1)$: deviations $(10/7,0,0)$; enter $x_1$ (pivot $3/7$) to basis $(x_3,x_1)$; all deviations $\le 0$. RHS: $x_3 = 5/4$, $x_1 = 11/4$, $x_2 = 0$. $Z = 3(11/4)+5/4 = 38/4 = 19/2$. **Answer:** $(11/4,0,5/4)$, $19/2$.

**Q9. Given:** Lec-11 closing slides. **Steps:** (1) Only $\bar{b}$, $\bar{P}_k$, $\pi$ computed, so less memory/arithmetic, suited to computers and large problems. (2) $\pi = c_B B^{-1}$ recorded every iteration; at optimum it is the dual solution and it is the input to sensitivity analysis (effect of data changes without resolving). **Answer:** As stated (2-4 sentences fulfilled).

**Q10. Given:** Symmetric pair definition (all $x, y \ge 0$, all inequality constraints; Max with $\le$, Min with $\ge$). **Steps:** Rules: (1) one $y_i \ge 0$ per primal row; (2) primal $c \to$ dual RHS; (3) primal $b \to$ dual costs; (4) $A \to A^T$; (5) flip inequality directions; (6) flip Max $\leftrightarrow$ Min. Applying twice: $(A^T)^T = A$, cost/RHS swap back, double flip restores directions and Max, $y$-variables map back to $x$. **Answer:** Dual of dual is primal.
