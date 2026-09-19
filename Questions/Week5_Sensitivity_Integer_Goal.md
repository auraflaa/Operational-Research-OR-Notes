# Week 5: Sensitivity II, Integer and Goal Programming (Lectures 21-25)

Coverage: sensitivity II ($a_{ij}$ changes, new/deleted variables and constraints, simultaneous changes), integer programming (IPP/MIPP, rounding failure, branch-and-bound, Gomory cuts), goal programming (deviational variables $u,v$, single-goal form, weighted vs preemptive multi-goal). Sources: Notes Module 2 Sec. 7, Notes Module 3 Lec 24-25, lec21-lec25 transcripts.

## Questions

**Q1.** In the dual simplex method, the criterion for the leaving variable is:

(a) most positive RHS
(b) most negative RHS
(c) largest deviation entry $\Delta_j$
(d) smallest ratio $\Delta_j / a_{rj}$ over $a_{rj} > 0$

*Source: Lecture 23 quiz*

**Q2.** Recall the Lec 20-21 product-mix example $\max Z = 2x_1 + 3x_2 + x_3$ with optimum basis $\{x_1, x_2\}$ and simplex multipliers $\pi = c_B B^{-1} = (5, 1)$. A new product D is proposed needing $1$ unit of labour and $1$ unit of material with profit $c_6 = 3$. Its deviation entry $\Delta_6 = c_6 - \pi P_6$ and the conclusion are:

(a) $\Delta_6 = -3 \le 0$; D is not profitable, basis unchanged
(b) $\Delta_6 = +2 > 0$; D should enter, re-solve
(c) $\Delta_6 = 0$; alternate optima with D in the basis
(d) $\Delta_6 = +8 > 0$; D replaces $x_1$ immediately

*Source: Lecture 21 in-lecture example*

**Q3.** Consider $\max z = 3x_1 + 4x_2$ s.t. $2x_1 + 4x_2 \le 13$, $-2x_1 + x_2 \le 2$, $2x_1 + 2x_2 \ge 1$, $6x_1 - 4x_2 \le 15$, $x_1, x_2 \ge 0$ integer. The LP relaxation optimum is $C = (7/2, 3/2)$, $z = 33/2$. Which statement is correct?

(a) Rounding $C$ gives $(4, 2)$ with $z = 20$, the integer optimum
(b) The four roundings of $C$ are $(3,1), (4,1), (4,2), (3,2)$; only $(3,1)$ with $z = 13$ is feasible, while the true integer optimum is $(2,2)$ with $z = 14$
(c) Rounding always recovers the integer optimum for two-variable problems
(d) The integer feasible set is convex, so $C$ rounded down to $(3,1)$ must be optimal

*Source: Lecture 24 in-lecture example*

**Q4.** Factory GP: $\min F = u + v$ s.t. $80x_1 + 40x_2 + u - v = 640$, $x_1 \le 6$, $x_2 \le 8$, $x_1, x_2, u, v \ge 0$, $u \cdot v = 0$. Let $f = 80x_1 + 40x_2$. Which statement is correct?

(a) Points with $f = 640$ form segment $DE$ with $D = (6,4)$, $E = (4,8)$; there $u = v = 0$, $F = 0$
(b) At any feasible point $u > 0$ and $v > 0$ simultaneously in the optimum
(c) The simplex method should bring $u$ and $v$ into the basis together
(d) The goal can never be met exactly because demand caps $6$ and $8$ are too tight

*Source: Lecture 25 in-lecture example*

**Q5.** The company multi-goal example (Lec 25) has goals $x_1 + x_2 + u_1 - v_1 = 80$, $x_1 + u_2 = 70$, $x_2 + u_3 = 45$, $x_1 + x_2 + u_4 - v_4 = 90$ with priorities $P_1 \gg P_2 \gg P_3 \gg P_4$. Which formulation is the preemptive (lexicographic) one?

(a) $\min F = 10u_1 + 8v_4 + 5u_2 + 3u_3 + v_1$ with a single objective row
(b) $\min F_1 = u_1$, then $\min F_2 = v_4$, then $\min F_3 = 5u_2 + 3u_3$, then $\min F_4 = v_1$, optimised lexicographically without degrading higher priorities
(c) $\min F = u_1 + v_1 + u_2 + u_3 + u_4 + v_4$ with equal weights
(d) $\min F = u_1 v_1 + u_4 v_4$ subject to $u_k v_k = 0$

**Q6.** Solve by branch-and-bound: $\max z = 3x_1 + 2x_2$ s.t. $x_1 \le 2$, $x_2 \le 2$, $x_1 + x_2 \le 3.5$, $x_1, x_2 \ge 0$ integer. Report the integer optimum $(x_1, x_2)$ and $z^*$.

*Source: Lecture 24 in-lecture example*

**Q7.** In the same product-mix example ($\pi = (5,1)$), a second proposal for D needs $2$ units of labour and $3$ units of material with profit $c_6 = 15$. Compute $\Delta_6 = c_6 - \pi P_6$ and state whether the current basis stays optimal.

*Source: Lecture 21 in-lecture example*

**Q8.** TV goal model: $\min F = u + v$ s.t. $800x_1 + 400x_2 + u - v = 24000$, $x_1 + x_2 \le 40$, $x_1 \le 24$, $x_2 \le 30$, $x_1, x_2, u, v \ge 0$, $u v = 0$. Evaluate $F$ at $(x_1, x_2) = (24, 12)$ and state whether the goal is exactly met.

*Source: Lecture 25 exercise*

**Q9.** State the sensitivity rules for (i) deleting a variable and (ii) deleting a constraint, distinguishing the case that leaves the optimum unchanged from the case that forces a re-solve.

**Q10.** Write the general single-goal linear GP form (goal equation, deviation variables, complementarity, real constraints), and explain in one sentence each how the weighted method and the preemptive method extend it to several goals.

*Source: Lecture 25 definitions; weighted/preemptive table*

## Answer key

| Q | Answer |
|---|---|
| 1 | (b) |
| 2 | (a) |
| 3 | (b) |
| 4 | (a) |
| 5 | (b) |
| 6 | $(2, 1)$, $z^* = 8$ |
| 7 | $\Delta_6 = +2 > 0$; basis no longer optimal, append column and re-iterate |
| 8 | $F = 0$; goal exactly met ($800(24) + 400(12) = 24000$) |
| 9 | See solution: non-basic/zero-basic deletion and loose-constraint deletion keep optimum; positive-basic deletion and tight-constraint deletion force re-solve |
| 10 | See solution: $\min u+v$, $f(x)+u-v=g$, $u v=0$ + hard constraints; weighted = one combined $F$, preemptive = lexicographic $F_1, F_2, \dots$ |

## Worked solutions

**Q1. Given:** Dual simplex starting point (deviations optimal, some RHS $< 0$). **Steps:** Lecture 23 rule: leaving variable first, chosen as the row with the most negative RHS; entering variable by the maximum-ratio test over negative pivot-row entries only (reverse of primal simplex). **Answer:** (b).

**Q2. Given:** $\pi = (5,1)$, $P_6 = (1,1)^T$, $c_6 = 3$. **Steps:** $\Delta_6 = 3 - (5,1)\cdot(1,1)^T = 3 - 6 = -3$. For a max problem optimality needs $\Delta_j \le 0$; $-3 \le 0$ passes, so appending D cannot raise $Z$. **Answer:** (a).

**Q3. Given:** LP optimum $(3.5, 1.5)$, $z = 16.5$. **Steps:** Neighbours $(3,1), (4,1), (4,2), (3,2)$; substituting into the five constraints leaves only $(3,1)$ feasible with $z = 3(3)+4(1) = 13$. Enumerating integer lattice points in polygon $ABCDEF$ gives $(2,2)$ feasible with $z = 6+8 = 14 > 13$. Hence rounding is unsafe; the IP set is discrete (non-convex). **Answer:** (b).

**Q4. Given:** Line $80x_1+40x_2 = 640$ cuts the $6 \times 8$ rectangle in segment $DE$: at $x_1 = 6$, $x_2 = 4$; at $x_2 = 8$, $x_1 = 4$. **Steps:** On $DE$, $f = 640$ so $u = v = 0$, $F = 0$. Above $DE$ ($DEC$ region) $v > 0, u = 0$; below ($OADEB$) $u > 0, v = 0$. Simplex must never have $u,v$ basic together ($u v = 0$); zero deviation on non-basic $x_3$ signals the multiple optima $D, E$ and all of $DE$. **Answer:** (a).

**Q5. Given:** Priorities $P_1$ (capacity under-use $u_1$), $P_2$ (overtime excess $v_4$), $P_3$ (sales shortfalls $5u_2+3u_3$), $P_4$ (overtime per se $v_1$). **Steps:** Weighted method collapses to one $F$ with numeric weights (option (a)); preemptive keeps one $F_i$ per level and minimises $F_1$, then $F_2$ without hurting $F_1$, etc., with one simplex objective row per priority. **Answer:** (b).

**Q6. Given:** LP0 relaxation. **Steps:** LP0 optimum $B = (2, 1.5)$, $z = 3(2)+2(1.5) = 9$; $x_2$ fractional so delete strip $1 < x_2 < 2$: LP01 ($+x_2 \le 1$) gives $(2,1)$, $z = 8$, integer, incumbent $8$; LP02 ($+x_2 \ge 2$) gives $(1.5,2)$, $z = 8.5$, bound $> 8$ but $x_1$ fractional, so branch $1 < x_1 < 2$: LP021 ($+x_1 \le 1$) gives $(1,2)$, $z = 7$, integer, worse; LP022 ($+x_1 \ge 2$ with $x_2 \ge 2$) violates $x_1+x_2 \le 3.5$, infeasible, fathomed. **Answer:** $(2,1)$, $z^* = 8$.

**Q7. Given:** $P_6 = (2,3)^T$, $c_6 = 15$. **Steps:** $\Delta_6 = 15 - (5,1)\cdot(2,3)^T = 15 - (10+3) = +2$. Since $+2 > 0$ in a max problem, the old basis is no longer optimal; append the $x_6$ column to the tableau and re-run simplex ($x_6$ enters). **Answer:** $+2$, re-solve needed.

**Q8. Given:** Profit $f = 800x_1+400x_2$, goal $24000$. **Steps:** At $(24,12)$: $f = 800(24)+400(12) = 19200+4800 = 24000$, so $f + u - v = 24000$ gives $u = v = 0$, $F = u+v = 0$. Caps satisfied ($24+12 = 36 \le 40$, $24 \le 24$, $12 \le 30$). Same holds at $(20,20)$ and all their convex combinations. **Answer:** $F = 0$, goal exactly achieved.

**Q9. Given:** Optimum tableau with basis values. **Steps:** (i) Deleting a non-basic variable, or a basic variable whose value is zero, changes nothing (the zero makes it effectively absent). Deleting a basic variable with positive value destroys a basis row: drop its column and basis entry, insert an artificial variable in that row, re-solve by two-phase/big-M. (ii) Deleting a constraint whose slack is positive (loose) at optimum leaves the optimum unchanged. Deleting a tight constraint (slack zero) may shift the optimum, so re-solve. **Answer:** As stated.

**Q10. Given:** Goal $g$ pre-fixed for objective $f(x)$. **Steps:** Single-goal GP: $\min F = u+v$ s.t. $f(x)+u-v = g$, hard system constraints $Ax\,(\le,=,\ge)\,b$, $x,u,v \ge 0$, $u\cdot v = 0$ ($u$ shortfall, $v$ excess). Weighted multi-goal: one combined $\min \sum_k(p_k u_k+q_k v_k)$, $p_k,q_k \ge 0$. Preemptive multi-goal: ranked $P_1 \gg P_2 \gg \cdots$ with one $F_i$ per level, minimised lexicographically. **Answer:** As stated.
