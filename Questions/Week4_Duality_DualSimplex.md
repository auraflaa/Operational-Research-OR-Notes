# Week 4: Duality Theorems, Dual Simplex and Sensitivity I (Lectures 16-20)

Coverage: asymmetric dual shortcuts ($=$ row $\to$ unrestricted $y$; unrestricted $x \to$ $=$ dual row), weak duality $f(X) \ge w(Y)$ and corollaries, optimality criterion, strong duality, complementary slackness (4 working conditions), multipliers $\pi = c_B B^{-1}$ as dual optimum, dual simplex algorithm, sensitivity to $c_j$ and $b_i$ (ranges, shadow prices). Sources: Notes Module 2, lec16-lec20 transcripts.

## Questions

**Q1.** Weak duality (Min primal $f(X) = C^T X$, $AX \ge B$, $X \ge 0$; Max dual $w(Y) = B^T Y$, $A^T Y \le C$, $Y \ge 0$) states that for any feasible pair $X, Y$:

(a) $f(X) = w(Y)$
(b) $f(X) \le w(Y)$
(c) $f(X) \ge w(Y)$, with $f - w = \sum_j x_j y_{m+j} + \sum_i y_i x_{n+i} \ge 0$ after adding slacks/surpluses
(d) no comparison is possible unless both are optimal

*Source: Lecture 16 exercise*

**Q2.** The primal Min $2x_1 - 11x_2$ s.t. $2x_1 + 3x_2 \ge 6$, $-x_1 \ge -5$, $x \ge 0$ is feasible with $f \to +\infty$. By weak-duality Corollary 3, its dual Max $6y_1 - 5y_2$ s.t. $2y_1 - y_2 \le 2$, $3y_1 \le -11$, $y \ge 0$ must be:

(a) feasible with equal value
(b) infeasible
(c) unbounded toward $-\infty$
(d) feasible with value $0$

*Source: Lecture 16 exercise*

**Q3.** At the optimum of a symmetric Max-primal/Min-dual pair, if a primal variable $x_j > 0$ then:

(a) the corresponding dual variable equals $0$
(b) the corresponding dual constraint holds as an equality
(c) the corresponding primal constraint is a strict inequality
(d) the corresponding dual constraint is a strict inequality

*Source: Lecture 17 exercise*

**Q4.** The dual simplex method applies when the tableau is dual-feasible but primal-infeasible. The leaving and entering rules (Min convention of Lecture 19) are:

(a) leaving: most negative RHS; entering: maximum ratio $\Delta_j / a_{rj}$ over $a_{rj} < 0$ in the pivot row
(b) leaving: largest positive $\Delta_j$; entering: minimum ratio $b_i / p_{ik}$ over $p_{ik} > 0$
(c) leaving: most negative $\Delta_j$; entering: minimum ratio over all columns
(d) leaving: smallest RHS; entering: first positive pivot-row entry

*Source: Lecture 19 exercise*

**Q5.** In Lecture 20's product-mix example (Max $2x_1+3x_2+x_3$, optimum basis $\{x_1,x_2\} = (1,2)$, $Z^* = 8$), raising labour availability from $1$ to $2$ gives $(x_1,x_2) = (5,1)$, $Z = 13$. If overtime labour costs Rs $4$/unit, the shadow price of labour and the hiring decision are:

(a) shadow price $4$; indifferent
(b) shadow price $5$; profitable to hire since $5 > 4$
(c) shadow price $8$; hire regardless
(d) shadow price $2$; do not hire

**Q6.** Primal Max $3x_1 + 5x_2$ s.t. $x_1 + 2x_2 \le 20$, $x_1 + x_2 \le 15$, $x \ge 0$; dual Min $20y_1 + 15y_2$ s.t. $y_1 + y_2 \ge 3$, $2y_1 + y_2 \ge 5$, $y \ge 0$. Solve both graphically and report both optima plus the final simplex multipliers.

*Source: Lecture 18 exercise*

**Q7.** Solve by dual simplex: Min $Z = x_1 + 4x_2 + 3x_4$ s.t. $x_1 + 2x_2 - x_3 + x_4 \ge 3$, $-2x_1 - x_2 + 4x_3 + x_4 \ge 2$, $x \ge 0$. Report the primal optimum and the multipliers $\pi = c_B B^{-1}$.

*Source: Lecture 19 exercise*

**Q8.** For the Lecture 20 example above (final $B^{-1} = [[4,-1],[-1,1]]$, deviations $(0,0,-3,-5,-1)$): (i) how high can the unit profit $c_3$ of product C rise before product C enters the basis? (ii) give the allowable range of labour availability $d$ (RHS $(d,3)$) keeping the basis $\{x_1,x_2\}$ optimal, and the profit $Z(d)$ in that range.

**Q9.** State the optimality-criterion theorem and the strong (main) duality theorem, and explain how the Lecture 17 example ($X = (0,0,4,4)$, $Y = (1.2,0.2)$, value $28$) illustrates the first.

**Q10.** A student claims "dual simplex is just primal simplex with Max and Min swapped." Correct this in 2-4 sentences: state the starting condition, the order of choices, the ratio-test reversal, and the infeasibility signal.

## Answer key

| Q | Answer |
|---|---|

| 1 | (c) |

| 2 | (b) |

| 3 | (b) |

| 4 | (a) |

| 5 | (b) |

| 6 | Primal $(10,5)$, $f^* = 55$; dual $(2,1)$, $w^* = 55$; multipliers $(0,0) \to (5,0) \to (2,1)$ |

| 7 | $x_1 = 7$, $x_3 = 4$, rest $0$, $Z^* = 7$; $\pi = (-2,-1/2)$ (lecture sign convention; dual optimum) |

| 8 | (i) $c_3 \le 4$ (at $c_3 = 6$, re-optimise to $(x_1,x_3) = (2,1)$, $Z = 10$); (ii) $3/4 \le d \le 3$, $Z = 5d + 3$ |

| 9 | See solution: equal feasible values $\Rightarrow$ optimal; feasible pair $\Rightarrow$ equal-value optima |

| 10 | See solution: dual-feasible/primal-infeasible start; leaving first (most negative RHS); max ratio over negative row entries; no negative entry $\Rightarrow$ infeasible |

## Worked solutions

**Q1. Given:** Symmetric Min/Max pair; proof adds surpluses $X_1$ to primal and slacks $Y_1$ to dual. **Steps:** Multiply primal rows by $y_i$, dual rows by $x_j$, add and subtract: $f - w = Y_1 X_0 + X_1 Y_0 \ge 0$ since all variables $\ge 0$. Hence every dual feasible value lower-bounds the primal minimum. (a) holds only at optimality; (b) reverses the inequality. **Answer:** (c).

**Q2. Given:** Lecture 16 Corollary-3 pair; primal ray makes $f \to +\infty$. **Steps:** If dual had any feasible $Y$, weak duality $f \ge w$ would still allow $f \to \infty$; the corollary's graphical check shows the dual's second constraint $3y_1 \le -11$ contradicts $y_1 \ge 0$, so no feasible $Y$ exists. (c) is the mirror corollary (dual unbounded $\Rightarrow$ primal infeasible). **Answer:** (b).

**Q3. Given:** Complementary slackness condition 1 of Lec 17, verified by $x_3 = 4 > 0$ forcing $2y_1 + 3y_2 = 3$ at $(1.2, 0.2)$. **Steps:** Positivity on one side forces equality on the other, at optimum only. Strict dual inequality would instead force $x_j = 0$ (condition 4). **Answer:** (b).

**Q4. Given:** Lecture 19 algorithm (Min convention: optimal when $\Delta_j \ge 0$; infeasible when some RHS $< 0$). **Steps:** Leaving first: most negative RHS ($-3$ before $-2$ in the worked example, so $x_5$ leaves). Entering: max ratio $\Delta_j/(-a_{rj})$ over $a_{rj} < 0$ only ($1/(-1), 4/(-2), 3/(-1) \to \max = -1$, so $x_1$ enters). Option (b) is primal simplex. **Answer:** (a).

**Q5. Given:** $Z: 8 \to 13$ for one extra labour unit. **Steps:** Shadow price $= \Delta Z / \Delta d = (13-8)/1 = 5$, valid while basis $\{x_1,x_2\}$ unchanged ($3/4 \le d \le 3$). Extra profit $5$ exceeds overtime cost $4$, so hiring is profitable. **Answer:** (b).

**Q6. Given:** Two-variable pair; slacks $x_3, x_4$ for primal simplex. **Steps:** Primal corners: $(0,0) \to 0$, $(0,10) \to 50$, $(15,0) \to 45$, intersection $x_1+2x_2 = 20$, $x_1+x_2 = 15 \Rightarrow (10,5) \to 55$. Max at $(10,5)$. Dual: $2y_1+y_2 = 5$, $y_1+y_2 = 3 \Rightarrow (2,1) \to 55$, minimum on the unbounded feasible region. Simplex multipliers: T1 $c_B = (0,0)$, $\pi = (0,0)$; T2 basis $\{x_2,x_4\}$, $c_B = (5,0)$, $\pi = (5,0)$; T3 basis $\{x_2,x_1\}$, $c_B = (5,3)$, $\pi = (2,1)$, matching the dual optimum with equal value $55$. **Answer:** Primal $(10,5) = 55$; dual $(2,1) = 55$.

**Q7. Given:** Two $\ge$ rows; add surpluses $x_5, x_6$, multiply by $-1$ for starting basis $\{x_5,x_6\}$, RHS $(-3,-2)$, deviations $(1,4,0,3,0,0)$. **Steps:** Iter 1: leave $x_5$ (most negative $-3$); max ratio $-1$ selects $x_1$; pivot ($R_1 \to -R_1$, $R_2 \to R_2 - 2R_1$) to basis $\{x_1,x_6\}$, RHS $(3,-8)$, deviations $(0,2,1,2,1,0)$. Iter 2: leave $x_6$ ($-8$); max ratio $-1/2$ selects $x_3$; pivot to basis $\{x_1,x_3\}$, RHS $(7,4)$, deviations $(0,1/2,0,1/2,2,1/2)$. All RHS $\ge 0$, all $\Delta \ge 0$: stop. $B^{-1} = [[-2,-1],[-1/2,-1/2]]$, $\bar{b} = (7,4)$, $\pi = (1,0)B^{-1} = (-2,-1/2)$. **Answer:** $x_1 = 7$, $x_3 = 4$, $Z^* = 7$.

**Q8. Given:** Optimum deviations $(0,0,-3,-5,-1)$, $B^{-1}$ as above. **Steps:** (i) $\Delta_3 = c_3 - (2,3)\cdot(-1,2)^T = c_3 - 4$; Max-optimality needs $\Delta_3 \le 0$, so $c_3 \le 4$. At $c_3 = 6$, $\Delta_3 = +2 > 0$; one pivot ($x_3$ in, $x_2$ out) gives basis $\{x_1,x_3\} = (2,1)$, $Z = 2(2)+6(1) = 10$. (ii) New RHS $\bar{b}^* = B^{-1}(d,3)^T = (4d-3, 3-d) \ge 0 \Rightarrow d \ge 3/4$, $d \le 3$. $x_1 = 4d-3$, $x_2 = 3-d$, $Z = 2(4d-3)+3(3-d) = 5d+3$. **Answer:** $c_3 \le 4$; $d \in [3/4, 3]$, $Z = 5d+3$.

**Q9. Given:** Symmetric pair; Lec-17 example primal Max $x_1+2x_2+3x_3+4x_4$ (RHS $20,20$), dual Min $20y_1+20y_2$ (4 $\ge$ rows). **Steps:** Optimality criterion: feasible $X, Y$ with $f(X) = \phi(Y)$ are both optimal. Here $X = (0,0,4,4)$ satisfies both $\le$ rows ($4+12 = 20$... check: row 1: $2(4)+3(4) = 20$; row 2: $3(4)+2(4) = 20$) with $f = 12+16 = 28$; $Y = (1.2,0.2)$ satisfies all four $\ge$ rows with $\phi = 24+4 = 28$. Equal values $\Rightarrow$ both optimal. Strong duality: feasibility of both guarantees equal-value optima exist. **Answer:** As stated.

**Q10. Given:** Lec-19 background. **Steps:** Dual simplex starts dual-feasible ($\Delta$ optimal) but primal-infeasible (RHS $< 0$) — the reverse of primal simplex. It picks the leaving row first (most negative RHS), then the entering column by maximum ratio over negative pivot-row entries only (primal uses minimum ratio over positive column entries). If the pivot row has no negative entry, the problem is infeasible. **Answer:** As stated.
