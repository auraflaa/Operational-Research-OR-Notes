# Mock Final Examination (100 marks, 3 hours)

Instructions: Answer all 25 questions. Part A: 10 MCQ, 2 marks each. Part B: 10 numerical-answer questions, 4 marks each. Part C: 5 short-answer/derivation questions, 8 marks each. Non-programmable calculator allowed. Show steps for Parts B and C.

Note: This is instructor-style practice assembled and adapted from the weekly question sets for NPTEL noc26_ma85 (Prof. Kusum Deep, IIT Roorkee). It is NOT a leaked paper and NOT an official sample paper; all numbers not marked verbatim have been changed and re-solved.

## Syllabus coverage (question to lectures)

| Question | Module | Topic | Lectures |
|---|---|---|---|
| A1 | 1 | OR model components / LPP definition | 1 |
| A2 | 1 | Graphical optimum (2-variable) | 3 |
| A3 | 1 | Big-M construction | 6 |
| A4 | 1 | Multiple optima signal in tableau | 8, 14 |
| A5 | 2 | Symmetric dual construction | 15 |
| A6 | 2 | Weak duality / complementary slackness | 16-17 |
| A7 | 3 | IPP rounding failure | 24 |
| A8 | 3 | Single-goal GP geometry | 25 |
| A9 | 4 | Transportation independent equations | 28 |
| A10 | 5 | Saddle / fair / strictly determinable; 2x2 formula | 36, 38 |
| B1 | 1 | Graphical Max with mixed constraints | 3 |
| B2 | 1 | Simplex on 2-variable Max | 5 |
| B3 | 2 | Primal-dual graphical pair + multipliers | 18 |
| B4 | 2 | New-variable deviation test | 21 |
| B5 | 3 | Branch-and-bound (2-variable IPP) | 24 |
| B6 | 3 | DP separable sum of squares | 27 |
| B7 | 4 | NW-corner IBFS cost | 28 |
| B8 | 4 | Johnson n x 2 elapsed time | 31 |
| B9 | 5 | 2x2 game value (oddments) | 38 |
| B10 | 5 | 2x2 game value (formula) | 38 |
| C1 | 1 | Standard form with free variable | 5 |
| C2 | 2 | Optimality criterion + strong duality (proof sketch + illustration) | 17 |
| C3 | 3 | Single-goal GP form, weighted vs preemptive, goal evaluation | 25 |
| C4 | 4 | MODI loop + degeneracy; n x 3 reduction | 28, 32 |
| C5 | 5 | Game-to-LPP pair, shift rule, solved 2x2 | 39 |

---

## Part A — MCQ (10 x 2 = 20 marks)

**A1.** Which statement about the general optimization model and LPPs is FALSE?

  a) The three components of an optimization model are decision variables, objective function, and constraints.
  b) If all of $f, g_k, h_j$ are linear the problem is linear programming; if any one is nonlinear it is nonlinear programming.
  c) An integer programming problem requires some or all decision variables to take integer values.
  d) Every linear programming problem must have exactly as many constraints as variables ($m = n$).

**A2.** Max $z = 4x_1 + 3x_2$ s.t. $x_1 + x_2 \leq 6$, $2x_1 + 5x_2 \leq 20$, $x_1, x_2 \geq 0$. The optimum is:

  a) $(0, 4)$, $z = 12$
  b) $(10/3, 8/3)$, $z = 64/3$
  c) $(6, 0)$, $z = 24$
  d) $(0, 0)$, $z = 0$

**A3.** A Max LPP has a $\geq$ row with no unit (basic) column after adding the surplus variable. The Big-M method:

  a) stops, since no initial BFS can ever be constructed.
  b) adds one artificial variable to that row and penalizes it by $-M$ ($M \to +\infty$) in the Max objective so it is driven to zero.
  c) adds one artificial variable to that row with reward $+M$ in the Max objective.
  d) pivots directly on the surplus column without any artificial variable.

**A4.** In the optimal tableau of a Max LPP, a non-basic variable has reduced cost $\bar{c}_j = 0$. This signals:

  a) an unbounded solution.
  b) an infeasible solution.
  c) multiple (alternate) optimal solutions obtainable by pivoting it in.
  d) a degenerate but necessarily unique solution.

**A5.** Primal: Max $z = 2x_1 + 3x_2$ s.t. $5x_1 - 2x_2 \geq 3$, $-2x_1 + x_2 \leq 4$, $x_1, x_2 \geq 0$. After normalising to Max-with-$\leq$ form, the symmetric dual is:

  a) Min $w = -3y_1 + 4y_2$ s.t. $-5y_1 - 2y_2 \geq 2$, $2y_1 + y_2 \geq 3$, $y_1, y_2 \geq 0$
  b) Max $w = -3y_1 + 4y_2$ s.t. $-5y_1 - 2y_2 \leq 2$, $2y_1 + y_2 \leq 3$, $y_1, y_2 \geq 0$
  c) Min $w = 3y_1 + 4y_2$ s.t. $5y_1 - 2y_2 \geq 2$, $-2y_1 + y_2 \geq 3$, $y_1, y_2 \geq 0$
  d) Min $w = 2y_1 + 3y_2$ s.t. $5y_1 - 2y_2 \geq -3$, $-2y_1 + y_2 \geq 4$, $y_1, y_2 \geq 0$

**A6.** For the symmetric pair Min $f(X) = C^T X$ s.t. $AX \geq B$, $X \geq 0$ and Max $w(Y) = B^T Y$ s.t. $A^T Y \leq C$, $Y \geq 0$, weak duality states that for any feasible pair $X, Y$:

  a) $f(X) = w(Y)$ always.
  b) $f(X) \leq w(Y)$.
  c) $f(X) \geq w(Y)$, with gap $f - w \geq 0$ (sum of complementary products after adding slacks/surpluses).
  d) no comparison is possible unless both are optimal.

**A7.** Which statement about solving integer programs by rounding the LP relaxation is correct?

  a) Rounding the LP optimum to the nearest integers always yields the integer optimum.
  b) Rounding can produce an infeasible point or a strictly worse feasible point; the integer feasible set is discrete (non-convex), so enumeration or branch-and-bound is needed.
  c) Rounding down (flooring) each variable always yields the integer optimum.
  d) The integer feasible set is convex, so some rounding of the LP optimum must be optimal.

**A8.** Factory goal model: Min $F = u + v$ s.t. $60x_1 + 30x_2 + u - v = 480$, $x_1 \leq 6$, $x_2 \leq 8$, $x_1, x_2, u, v \geq 0$, $u v = 0$. Let $f = 60x_1 + 30x_2$. Which is correct?

  a) Points with $f = 480$ form the segment $DE$ with $D = (6, 4)$, $E = (4, 8)$; there $u = v = 0$ and $F = 0$.
  b) At any optimum $u > 0$ and $v > 0$ simultaneously.
  c) The simplex method should bring $u$ and $v$ into the basis together.
  d) The goal can never be met because the caps $6$ and $8$ are too tight.

**A9.** In a balanced transportation problem with $3$ origins and $4$ destinations, the number of linearly independent constraint equations is:

  a) $12$
  b) $7$
  c) $6$
  d) $3$

**A10.** Which pair of statements is correct?

  a) A game with maximin = minimax $= 0$ is strictly determinable; one with maximin = minimax $= V$ is fair.
  b) A game with maximin = minimax $= 0$ is fair; one with maximin = minimax $= V$ (saddle exists) is strictly determinable.
  c) Every matrix game has a saddle point, so pure strategies always suffice.
  d) A game with no saddle point has no value.

---

## Part B — Numerical answers (10 x 4 = 40 marks)

**B1.** Solve graphically: Max $4x + 7y$ s.t. $2x + 3y \leq 36$, $x + 2y \geq 12$, $x, y \geq 0$. Give the optimum point and optimum value.

**B2.** Solve by simplex (or graphically with tableau check): Max $3x_1 + 5x_2$ s.t. $x_1 + 2x_2 \leq 12$, $3x_1 + 2x_2 \leq 18$, $x_1, x_2 \geq 0$. Give the optimum point and optimum value.

**B3.** Primal Max $4x_1 + 3x_2$ s.t. $x_1 + 2x_2 \leq 16$, $2x_1 + x_2 \leq 20$, $x \geq 0$; dual Min $16y_1 + 20y_2$ s.t. $y_1 + 2y_2 \geq 4$, $2y_1 + y_2 \geq 3$, $y \geq 0$. Solve both graphically and report both optima.

**B4.** At some Max optimum the simplex multipliers are $\pi = (4, 2)$. A proposed product D needs $P_6 = (2, 1)^T$ units of the two resources with unit profit $c_6 = 12$. Compute $\Delta_6 = c_6 - \pi P_6$ and state whether the current basis stays optimal.

**B5.** Solve by branch-and-bound: Max $z = 4x_1 + 3x_2$ s.t. $x_1 \leq 2$, $x_2 \leq 2$, $x_1 + x_2 \leq 3.5$, $x_1, x_2 \geq 0$ integer. Report the integer optimum and $z^*$.

**B6.** Solve by dynamic programming: Min $z = u_1^2 + u_2^2 + u_3^2$ s.t. $u_1 + u_2 + u_3 \geq 60$, $u_j \geq 0$. Report the optimal $(u_1, u_2, u_3)$ and $z^*$.

**B7.** A balanced $3 \times 4$ transportation problem has supplies $a = [7, 9, 18]$, demands $b = [5, 8, 7, 14]$, and costs $c_{11} = 15$, $c_{12} = 25$, $c_{22} = 20$, $c_{23} = 30$, $c_{33} = 60$, $c_{34} = 15$. The NW-corner rule gives allocations $x_{11} = 5$, $x_{12} = 2$, $x_{22} = 6$, $x_{23} = 3$, $x_{33} = 4$, $x_{34} = 14$. Compute the IBFS cost $Z_{NW}$.

**B8.** Five jobs through machines A then B have times (hours) $A = [4, 2, 8, 6, 9]$, $B = [3, 7, 5, 9, 4]$. Using Johnson's rule, the minimum total elapsed time $T$ is _____ hours. (Give $T$ and one optimal sequence.)

**B9.** For $A = \begin{pmatrix} 5 & 2 \\ 3 & 4 \end{pmatrix}$, confirm there is no saddle point and compute the value $V$ (exact fraction).

**B10.** For $A = \begin{pmatrix} 2 & 5 \\ 8 & 3 \end{pmatrix}$, confirm there is no saddle point and compute the value $V$ (exact fraction).

---

## Part C — Short answer / derivations (5 x 8 = 40 marks)

**C1 (Module 1).** Convert to standard form: Min $2x_1 - 4x_2 + 2x_3$ s.t. $2x_1 - x_2 + x_3 \leq 5$, $x_1 + 3x_2 \geq -8$, $-3x_1 + 2x_2 + 5x_3 \leq 6$, $x_1, x_2 \geq 0$, $x_3$ unrestricted. Show each step (objective flip, RHS fix, slacks, free-variable split) and write the final Max problem with equalities.

**C2 (Module 2).** State the optimality-criterion theorem and the strong (main) duality theorem for the symmetric Max/Min pair. Then verify them on the B3 pair: show primal $(8, 4)$ and dual $(2/3, 5/3)$ are feasible, compute both objective values, and explain why equality certifies optimality.

**C3 (Module 3).** (a) Write the general single-goal linear GP form (goal equation, deviational variables, complementarity, hard constraints). (b) State in one sentence each how the weighted method and the preemptive method extend it to several goals. (c) Evaluate the TV-style model Min $F = u + v$ s.t. $600x_1 + 300x_2 + u - v = 18000$, $x_1 + x_2 \leq 40$, $x_1 \leq 24$, $x_2 \leq 30$, $x, u, v \geq 0$ at $(x_1, x_2) = (20, 20)$: compute $F$ and state whether the goal is met.

**C4 (Module 4).** (a) Define a loop in a transportation tableau and explain how it is used with the MODI test to improve a non-optimal BFS, including the degeneracy fix when occupied cells are fewer than $m + n - 1$. (b) State the $n \times 3$ reducibility condition (order ABC), give $G = A + B$, $H = B + C$, and state how the optimal sequence is obtained; what if neither condition holds?

**C5 (Module 5).** (a) Write the LPP pair for a general $m \times n$ game after $x_i = p_i / V$, $y_j = q_j / V$ (assume shifted $V' > 0$), state the primal-dual relationship and which LP is solved in practice and why. (b) State the constant-shift fix for negative entries. (c) Solve the B9 game $A = \begin{pmatrix} 5 & 2 \\ 3 & 4 \end{pmatrix}$ by oddments/formula: give $p, q, V$ with checks.

---

## Answer key

| Q | Answer |
|---|---|
| A1 | (d) |
| A2 | (c) $(6,0)$, $24$ |
| A3 | (b) |
| A4 | (c) |
| A5 | (a) |
| A6 | (c) |
| A7 | (b) |
| A8 | (a) |
| A9 | (c) $6$ |
| A10 | (b) |
| B1 | $(0, 12)$, max $84$ |
| B2 | $(3, 9/2)$, max $63/2 = 31.5$ |
| B3 | Primal $(8, 4) = 44$; dual $(2/3, 5/3) = 44$ |
| B4 | $\Delta_6 = +2 > 0$; basis no longer optimal, append column and re-iterate |
| B5 | $(2, 1)$, $z^* = 11$ |
| B6 | $(20, 20, 20)$, $z^* = 1200$ |
| B7 | $Z_{NW} = 785$ |
| B8 | $T = 32$ h (e.g. 2-4-3-5-1) |
| B9 | $V = 7/2$ |
| B10 | $V = 17/4$ |
| C1 | Max $-2x_1 + 4x_2 - 2x_4 + 2x_5$ s.t. three equalities, all vars $\geq 0$ (see solution) |
| C2 | Equal feasible values imply optimality; feasible pair implies equal-value optima; B3 values both $44$ |
| C3 | $\min u+v$, $f(x)+u-v=g$, $uv=0$ + hard constraints; weighted = one combined $F$, preemptive = lexicographic; $F=0$, goal met |
| C4 | Loop + $\theta$-shift + $\epsilon$-zero; $G/H$ + Johnson; else method fails |
| C5 | A: $\min\sum x_i$ s.t. $\geq 1$; B: $\max\sum y_j$ s.t. $\leq 1$; duals, solve B's LP; $p=(1/4,3/4)$, $q=(1/2,1/2)$, $V=7/2$ |

---

## Worked solutions

**A1. Given:** general model Min/Max $f(X)$, $X \in S$. **Steps:** Components are (a); linear/nonlinear split is (b); integer restriction is (c). LPP definition has $m, n$ positive integers with generally $m \neq n$, so (d) is false. **Answer:** (d).

**A2. Given:** Max $4x_1 + 3x_2$; lines $x_1 + x_2 = 6$ through $(0,6),(6,0)$ and $2x_1 + 5x_2 = 20$ through $(0,4),(10,0)$. **Steps:** Corners $O(0,0) \to 0$, $A(0,4) \to 12$, $B(10/3,8/3) \to 40/3 + 8 = 64/3 \approx 21.3$, $C(6,0) \to 24$. Farthest iso-profit line touches $C$. **Answer:** (c).

**A3. Given:** $\geq$ row lacks a starting unit column. **Steps:** Surplus $-x_s$ gives no unit column, so one artificial per such row supplies the BFS, penalized $-M$ in Max so the maximizer forces it to zero. (c) has the wrong sign; (a)/(d) describe no valid start. **Answer:** (b).

**A4. Given:** Optimal Max tableau, non-basic $\bar{c}_j = 0$. **Steps:** That variable can enter without changing $z$; pivoting yields a second corner and the whole edge is optimal. Ratio-test failure is unbounded; artificial $> 0$ in basis is infeasible. **Answer:** (c).

**A5. Given:** Max with one $\geq$ row. **Steps:** Normalise to all-$\leq$: multiply row 1 by $-1$ to get $-5x_1 + 2x_2 \leq -3$; row 2 unchanged. Six rules (one $y_i \geq 0$ per row; costs $(-3, 4)$; RHS $(2, 3)$; $A^T$; Max $\to$ Min; $\leq \to \geq$): Min $-3y_1 + 4y_2$ s.t. $-5y_1 - 2y_2 \geq 2$, $2y_1 + y_2 \geq 3$, $y \geq 0$. **Answer:** (a).

**A6. Given:** Symmetric Min/Max pair with added surpluses/slacks. **Steps:** Multiplying out gives $f - w$ as a sum of non-negative complementary products, so every dual value lower-bounds the primal minimum. (a) holds only at optimality; (b) reverses it. **Answer:** (c).

**A7. Given:** Lecture 24 rounding example. **Steps:** Neighbour roundings of an LP optimum can violate a constraint or lose value (there the only feasible rounding gave $13$ while the true integer optimum was $14$); the IP set is discrete, hence non-convex. **Answer:** (b).

**A8. Given:** Line $60x_1 + 30x_2 = 480$ cuts the $6 \times 8$ rectangle at $D = (6,4)$ and $E = (4,8)$. **Steps:** On $DE$, $f = 480$ so $u = v = 0$, $F = 0$; off it exactly one deviation is positive ($uv = 0$ must hold, so they never enter together). Caps allow $DE$, so the goal is attainable. **Answer:** (a).

**A9. Given:** Balanced $m \times n$ transport; only $m + n - 1$ of the $m + n$ equations are independent. **Steps:** $3 + 4 - 1 = 6$. **Answer:** (c).

**A10. Given:** Lecture 36 definitions. **Steps:** Fair means common value $0$; strictly determinable means maximin = minimax $= V$ via a saddle. No-saddle games still have a value in mixed strategies by the fundamental theorem. **Answer:** (b).

**B1. Given:** Max $4x + 7y$, $2x + 3y \leq 36$ (origin feasible), $x + 2y \geq 12$ (origin infeasible). **Steps:** Line 1 through $(18,0),(0,12)$; line 2 through $(12,0),(0,6)$; intersection at $y = -12$ outside quadrant. Corners $(12,0) \to 48$, $(18,0) \to 72$, $(0,12) \to 84$, $(0,6) \to 42$. **Answer:** $(0,12)$, max $84$.

**B2. Given:** Max $3x_1 + 5x_2$ with slacks $x_3, x_4$. **Steps:** Corners $(0,0) \to 0$, $(0,6) \to 30$, $(6,0) \to 18$, intersection $x_1 + 2x_2 = 12$, $3x_1 + 2x_2 = 18 \Rightarrow x_2 = 9/2$, $x_1 = 3 \to 9 + 45/2 = 63/2$. Simplex enters $x_2$ then $x_1$, ending with basis $\{x_2 = 9/2, x_1 = 3\}$, deviations $\leq 0$. **Answer:** $(3, 9/2)$, max $63/2$.

**B3. Given:** Two-variable pair. **Steps:** Primal corners $(0,0) \to 0$, $(0,8) \to 24$, $(10,0) \to 40$, intersection $x_1 + 2x_2 = 16$, $2x_1 + x_2 = 20 \Rightarrow (8,4) \to 32 + 12 = 44$, the max. Dual intersection $y_1 + 2y_2 = 4$, $2y_1 + y_2 = 3 \Rightarrow (2/3,5/3) \to 32/3 + 100/3 = 44$, the min on the unbounded dual region. Multipliers run $(0,0) \to$ dual-infeasible $\to (2/3,5/3)$. **Answer:** primal $(8,4) = 44$; dual $(2/3,5/3) = 44$.

**B4. Given:** $\pi = (4,2)$, $P_6 = (2,1)^T$, $c_6 = 12$. **Steps:** $\Delta_6 = 12 - (4,2)\cdot(2,1)^T = 12 - 10 = +2$. Max-optimality needs $\Delta \leq 0$; $+2 > 0$ fails. **Answer:** $+2$; append the $x_6$ column and re-iterate ($x_6$ enters).

**B5. Given:** LP0 relaxation. **Steps:** LP0 optimum $(2, 3/2)$, $z = 8 + 9/2 = 25/2$; $x_2$ fractional, delete strip $1 < x_2 < 2$: LP01 ($+x_2 \leq 1$) gives $(2,1)$, $z = 11$, integer incumbent; LP02 ($+x_2 \geq 2$) gives $(3/2,2)$, $z = 12$, bound above incumbent but $x_1$ fractional, branch $1 < x_1 < 2$: LP021 ($+x_1 \leq 1$) gives $(1,2)$, $z = 10$ (worse); LP022 ($+x_1 \geq 2$, $+x_2 \geq 2$) violates $x_1 + x_2 \leq 3.5$, infeasible. **Answer:** $(2,1)$, $z^* = 11$.

**B6. Given:** $F_1(x_1) = x_1^2$, $F_2(x_2) = \min_{u_2}[u_2^2 + (x_2-u_2)^2]$, $F_3(x_3) = \min_{u_3}[u_3^2 + F_2(x_3-u_3)]$. **Steps:** $F_2$: $u_2 = x_2/2$, $F_2 = x_2^2/2$. $F_3$: $u_3 = x_3/3$, $F_3 = x_3^2/3$. Smallest feasible $x_3 = 60$ gives $3600/3 = 1200$ with $u_3 = 20$, $u_2 = 20$, $u_1 = 20$. **Answer:** $(20,20,20)$, $1200$.

**B7. Given:** Balanced ($34 = 34$); NW allocations as stated. **Steps:** Rows $5 + 2 = 7$, $6 + 3 = 9$, $4 + 14 = 18$; columns $5$, $2 + 6 = 8$, $3 + 4 = 7$, $14$. Cost $5(15) + 2(25) + 6(20) + 3(30) + 4(60) + 14(15) = 75 + 50 + 120 + 90 + 240 + 210 = 785$. **Answer:** $785$.

**B8. Given:** $A = [4,2,8,6,9]$, $B = [3,7,5,9,4]$, order AB. **Steps:** Johnson: $\min = 2 = A_2 \to$ job 2 first; $\min = 3 = B_1 \to$ job 1 last $[2,\_,\_,\_,1]$; $\min = 4 = B_5 \to$ job 5 fourth $[2,\_,\_,5,1]$; of jobs 3,4 $\min = 5 = B_3 \to$ job 3 third $[2,\_,3,5,1]$; job 4 middle $\to$ 2-4-3-5-1. Chain: J2 A 0-2, B 2-9; J4 A 2-8, B 9-18; J3 A 8-16, B 18-23; J5 A 16-25, B 25-29; J1 A 25-29, B 29-32. **Answer:** $T = 32$ h.

**B9. Given:** $A = \begin{pmatrix} 5 & 2 \\ 3 & 4 \end{pmatrix}$. **Steps:** Row minima $2, 3 \to$ maximin $3$; column maxima $5, 4 \to$ minimax $4$; unequal, no saddle. $D = 5 + 4 - 2 - 3 = 4$. $p_1 = (4-3)/4 = 1/4$, $p_2 = 3/4$; $q_1 = (4-2)/4 = 1/2$, $q_2 = 1/2$; $V = (5\cdot 4 - 2\cdot 3)/4 = 14/4 = 7/2$. Checks: rows $5/4 + 9/4 = 7/2$, $2/4 + 12/4 = 7/2$; columns $5/2 + 1 = 7/2$, $3/2 + 2 = 7/2$. **Answer:** $7/2$.

**B10. Given:** $A = \begin{pmatrix} 2 & 5 \\ 8 & 3 \end{pmatrix}$. **Steps:** Row minima $2, 3 \to$ maximin $3$; column maxima $8, 5 \to$ minimax $5$; no saddle. $D = 2 + 3 - 5 - 8 = -8$. $p_1 = (3-8)/(-8) = 5/8$, $p_2 = 3/8$; $q_1 = (3-5)/(-8) = 1/4$, $q_2 = 3/4$; $V = (2\cdot 3 - 5\cdot 8)/(-8) = 34/8 = 17/4$. Checks: rows $10/8 + 24/8 = 34/8$; columns $2/4 + 24/4 = 34/8$. **Answer:** $17/4$.

**C1. Given:** Min with mixed constraints and free $x_3$. **Steps:** (i) Objective: Max $-2x_1 + 4x_2 - 2x_3$. (ii) Row 2 RHS $-8 < 0$: multiply by $-1$ to get $-x_1 - 3x_2 \leq 8$. (iii) All three $\leq$ rows: add slacks $x_6, x_7, x_8$. (iv) Free $x_3 = x_4 - x_5$, $x_4, x_5 \geq 0$, substituted everywhere. **Answer:** Max $-2x_1 + 4x_2 - 2x_4 + 2x_5$ s.t. $2x_1 - x_2 + x_4 - x_5 + x_6 = 5$, $-x_1 - 3x_2 + x_7 = 8$, $-3x_1 + 2x_2 + 5x_4 - 5x_5 + x_8 = 6$, all variables $\geq 0$.

**C2. Given:** Symmetric Max-primal/Min-dual pair. **Steps:** Optimality criterion: feasible $X, Y$ with $f(X) = \phi(Y)$ are both optimal. Strong duality: if both are feasible, equal-value optima exist. Check B3: primal $(8,4)$: $8 + 8 = 16 \leq 16$, $16 + 4 = 20 \leq 20$, $f = 32 + 12 = 44$; dual $(2/3,5/3)$: $2/3 + 10/3 = 4 \geq 4$, $4/3 + 5/3 = 3 \geq 3$, $w = 32/3 + 100/3 = 44$. Equal values certify both optimal. **Answer:** as stated.

**C3. Given:** Goal $g$ pre-fixed for $f(x)$. **Steps:** (a) Single-goal GP: $\min F = u + v$ s.t. $f(x) + u - v = g$, hard constraints $Ax\,(\leq,=,\geq)\,b$, $x, u, v \geq 0$, $u v = 0$ ($u$ shortfall, $v$ excess). (b) Weighted: one combined $\min \sum_k (p_k u_k + q_k v_k)$. Preemptive: ranked $P_1 \gg P_2 \gg \cdots$ with one $F_i$ per level, minimised lexicographically. (c) At $(20,20)$: $f = 600(20) + 300(20) = 18000$, so $u = v = 0$, $F = 0$; caps $20 + 20 = 40 \leq 40$ satisfied. **Answer:** $F = 0$, goal exactly achieved.

**C4. Given:** Lectures 28 and 32. **Steps:** (a) A loop is a cell sequence where consecutive cells share a row or column, no three consecutive share a row/column, first and last share a row/column, no cell repeats. If some non-basic $r_{ij} < 0$, form its unique loop with basic cells, shift $\theta$ (minimum at minus corners) alternately, re-test MODI until all $r_{ij} \geq 0$. Degeneracy (occupied $< m + n - 1$ from simultaneous exhaustion): add $\epsilon$-zero in the cheapest independent non-loop cell before MODI. (b) $n \times 3$ (order ABC) reduces via $G_i = A_i + B_i$, $H_i = B_i + C_i$ plus Johnson only if $\min A \geq \max B$ or $\min C \geq \max B$. Use that sequence on the original problem and chain in/out for $T$. If neither holds, no general Johnson-type procedure applies. **Answer:** as stated.

**C5. Given:** Game-to-LP conversion with $V' > 0$. **Steps:** (a) A (primal): $\min Z_p = \sum_i x_i$ s.t. $\sum_i a_{ij} x_i \geq 1$ per B-column $j$, $x \geq 0$. B (dual): $\max Z_q = \sum_j y_j$ s.t. $\sum_j a_{ij} y_j \leq 1$ per A-row $i$, $y \geq 0$. Duals of each other with $Z_p^* = Z_q^* = 1/V'$; recover $V' = 1/Z^*$, $p_i = x_i V'$, $q_j = y_j V'$. Solve B's $\leq$-LP (slacks only, no artificials) and read A's solution as the dual. (b) If entries are negative / $V \leq 0$: add constant $k$ to every entry, solve, carry strategies over, $V_{\text{orig}} = V_{\text{new}} - k$. (c) B9: no saddle ($3 \neq 4$); $D = 4$; $p = (1/4, 3/4)$, $q = (1/2, 1/2)$, $V = 7/2$ with row/column checks as in B9. **Answer:** as stated.
