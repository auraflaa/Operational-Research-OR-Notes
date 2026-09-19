# Week 6: Multi-Objective, DP, Transportation and Assignment (Lectures 26-30)

Coverage: multi-objective programming (ideal vs efficient solutions, efficiency cone, unique-minimizer theorem, weighting method), dynamic programming (Bellman's principle, stage/state/decision/transformation, backward recursion, additive and multiplicative examples), transportation (balanced vs unbalanced, NW-corner, least-cost, VAM, loop, MODI/u-v test), assignment (formulation, Hungarian method, unbalanced/maximization variants). Sources: Notes Module 3 Lec 26-27, Notes Module 4 Lec 28-30, lec26-lec30 transcripts.

## Questions

**Q1.** Consider the theorem from Lecture 26: if $X^0$ is a unique minimizer of one objective $f_i$ in a multi-objective problem, then $X^0$ is an efficient solution, but the converse is false. This statement is:

    a) True; Case 3 of the lecture ($B = (3,2)$ efficient but tying on $AB$ for $f_1$ and on $BC$ for $f_2$) is the counter-example to the converse
    b) False; a unique minimizer of one objective is never efficient
    c) True; and the converse is also always true
    d) False; efficiency implies unique minimization of every objective

*Source: Lecture 30 quiz Q8 (theorem from Lecture 26)*

**Q2.** In a balanced transportation problem with $4$ origins and $5$ destinations, the number of linearly independent constraint equations is:

    a) $20$
    b) $9$
    c) $8$
    d) $4$

*Source: Lecture 30 quiz Q12*

**Q3.** In the Hungarian method for an $n \times n$ assignment problem, the current reduced matrix is optimal when:

    a) the number of zeros equals $n$
    b) the minimum number of horizontal and vertical lines covering all zeros equals $n$ (the number of jobs), with assignment made at zero positions
    c) every row contains at least two zeros
    d) the smallest uncovered entry is zero

*Source: Lecture 30 quiz Q15*

**Q4.** Which of the following statements is correct?

    a) A transportation problem is a special type of assignment problem
    b) An assignment problem is a special case of a transportation problem with $m = n$ and all supplies and demands equal to $1$; a transportation problem is a special type of LPP
    c) Transportation and assignment problems cannot be written as linear programs
    d) An unbalanced assignment problem has no feasible solution even after adding dummies

*Source: Lecture 30 quiz Q11 and Q13*

**Q5.** A basic feasible solution of a minimization transportation problem with dual variables $u_i, v_j$ satisfying $u_i + v_j = c_{ij}$ on basic cells is optimal if and only if:

    a) all opportunity costs $r_{ij} = c_{ij} - u_i - v_j$ on non-basic cells satisfy $r_{ij} \ge 0$; VAM usually gives the lowest IBFS cost of the three methods but is not guaranteed optimal
    b) all $r_{ij} \le 0$ on basic cells
    c) the NW-corner cost is lower than the VAM cost
    d) the number of occupied cells exceeds $m + n - 1$

**Q6.** Determine the ideal and the efficient solutions of: $\max f_1 = 5x_1 + 4x_2$, $\max f_2 = 3x_1 - 2x_2$ subject to $x_1 + 2x_2 \le 4$, $-x_1 + x_2 \le 1$, $x_1, x_2 \ge 0$. Report $f_1, f_2$ at each extreme point.

*Source: Lecture 30 case study*

**Q7.** Solve by dynamic programming: $\min z = u_1^2 + u_2^2 + u_3^2$ subject to $u_1 + u_2 + u_3 \ge 100$, $u_j \ge 0$. Report the optimal $(u_1, u_2, u_3)$ and $z^*$.

*Source: Lecture 27 in-lecture example*

**Q8.** A balanced $3 \times 4$ transportation problem has supplies $a = [7, 9, 18]$, demands $b = [5, 8, 7, 14]$, and costs $c_{11} = 19$, $c_{12} = 30$, $c_{22} = 30$, $c_{23} = 40$, $c_{33} = 70$, $c_{34} = 20$. The NW-corner rule gives allocations $x_{11} = 5$, $x_{12} = 2$, $x_{22} = 6$, $x_{23} = 3$, $x_{33} = 4$, $x_{34} = 14$. Compute the IBFS cost $Z_{NW}$.

*Source: Lecture 28 in-lecture example*

**Q9.** State Bellman's principle of optimality and define stage, decision, state, state transformation, and the backward recursion for a separable additive problem with one $\ge$ constraint.

**Q10.** Define a loop in a transportation tableau and explain, in 2-4 sentences, how it is used with the MODI test to improve a non-optimal BFS, including the degeneracy fix when occupied cells are fewer than $m + n - 1$.

## Answer key

| Q | Answer |
|---|---|
| 1 | (a) |
| 2 | (c) |
| 3 | (b) |
| 4 | (b) |
| 5 | (a) |
| 6 | Ideal: $A = (4,0)$ ($f_1 = 20$, $f_2 = 12$); efficient: $O = (0,0)$, $B = (2/3,5/3)$, $C = (0,1)$ (no ideal besides $A$) |
| 7 | $u_1 = u_2 = u_3 = 100/3$, $z^* = 10000/3 \approx 3333.3$ |
| 8 | $Z_{NW} = 1015$ |
| 9 | See solution: Bellman statement; $j, u_j, x_j, x_{j-1} = t_j(x_j,u_j), F_j(x_j) = \mathrm{opt}_{u_j}[f_j(u_j) + F_{j-1}(x_{j-1})]$ |
| 10 | See solution: loop definition; shift $\theta$ at alternate corners; $\epsilon$-zero in cheapest independent non-loop cell |

## Worked solutions

**Q1. Given:** Lecture 26 theorem and Case 3 ($f_1 = -(2x_1 - x_2)$, $f_2 = -(x_1 + x_2)$, both minimized at $B = (3,2)$ but tied along $AB$ and $BC$ respectively). **Steps:** A unique single-objective minimizer cannot be dominated (any dominator would beat that objective), so it is efficient. Case 3 shows $B$ efficient yet not a unique minimizer of either objective, refuting the converse. Options (b)-(d) reverse or overstate the logic. **Answer:** (a).

**Q2. Given:** Balanced $m \times n$ transportation; only $m + n - 1$ of the $m + n$ row/column equations are independent. **Steps:** $m + n - 1 = 4 + 5 - 1 = 8$. Option (b) counts all $m + n$ equations without the dependency; (a) counts cells. **Answer:** (c).

**Q3. Given:** Hungarian stopping rule (Lec 29 step 3). **Steps:** Cover all zeros with the minimum possible horizontal plus vertical lines; optimality holds iff that minimum equals $n$, then assign at zero positions. Counting zeros (a) is insufficient since zeros may share lines; (d) describes the adjustment trigger, not optimality. **Answer:** (b).

**Q4. Given:** Lec 28-29 hierarchy: transport is a structured LPP; assignment is transport with $m = n$, $a_i = b_j = 1$, $x_{ij} \in \{0,1\}$. **Steps:** (a) reverses the hierarchy. (c) is false since both are LPPs. (d) is false: unbalanced cases are balanced with zero-cost dummies. **Answer:** (b).

**Q5. Given:** Dual $\max \sum a_i u_i + \sum b_j v_j$ s.t. $u_i + v_j \le c_{ij}$; complementary slackness $x_{ij}(u_i + v_j - c_{ij}) = 0$. **Steps:** Basics satisfy $u_i + v_j = c_{ij}$; non-basic opportunity costs $r_{ij} = c_{ij} - u_i - v_j \ge 0$ certify optimality (minimization). On the lecture's first dataset $Z_{VAM} = 779 < Z_{LC} = 814 < Z_{NW} = 1015$, so VAM starts closest, but closeness is empirical, not an optimality guarantee. **Answer:** (a).

**Q6. Given:** Feasible polygon $O = (0,0)$, $A = (4,0)$, $B = (2/3,5/3)$, $C = (0,1)$ from $x_1 + 2x_2 = 4$ and $-x_1 + x_2 = 1$ intersecting at $(2/3, 5/3)$. **Steps:** $f_1$: $O: 0$, $A: 20$, $B: 5(2/3) + 4(5/3) = 30/3 = 10$, $C: 4$; maximum at $A$. $f_2$: $O: 0$, $A: 12$, $B: 3(2/3) - 2(5/3) = 2 - 10/3 = -4/3$, $C: -2$; maximum at $A$. Since both maxima coincide at $A$, $A$ is the ideal solution; $O, B, C$ are non-dominated (efficient). **Answer:** Ideal $A = (4,0)$; efficient $O, B, C$.

**Q7. Given:** Separable additive DP with $x_3 = u_1+u_2+u_3 \ge 100$, $x_2 = x_3 - u_3$, $x_1 = x_2 - u_2$; $F_1(x_1) = x_1^2$, $F_2(x_2) = \min_{u_2}[u_2^2 + (x_2-u_2)^2]$, $F_3(x_3) = \min_{u_3}[u_3^2 + F_2(x_3-u_3)]$. **Steps:** $F_2$: $2u_2 - 2(x_2-u_2) = 0 \Rightarrow u_2 = x_2/2$, $F_2 = x_2^2/2$. $F_3$: $\min_{u_3}[u_3^2 + (x_3-u_3)^2/2]$; $2u_3 - (x_3-u_3) = 0 \Rightarrow u_3 = x_3/3$, $F_3 = x_3^2/3$. Smallest feasible $x_3 = 100$ gives $F_3 = 10000/3$ with $u_3 = 100/3$, $u_2 = (200/3)/2 = 100/3$, $u_1 = 100/3$. (The lecture audio says $1000$ here, an arithmetic slip; $100^2/3 = 10000/3$.) **Answer:** $(100/3, 100/3, 100/3)$, $z^* = 10000/3$.

**Q8. Given:** Balanced ($34 = 34$); NW allocations as stated. **Steps:** Row checks: $5+2 = 7$, $6+3 = 9$, $4+14 = 18$; column checks: $5$, $2+6 = 8$, $3+4 = 7$, $14$. Cost: $5(19) + 2(30) + 6(30) + 3(40) + 4(70) + 14(20) = 95 + 60 + 180 + 120 + 280 + 280 = 1015$. **Answer:** $1015$.

**Q9. Given:** Lec 27 definitions for $\min \sum_j f_j(u_j)$ s.t. $\sum_j a_j u_j \ge b$, $a_j, b > 0$. **Steps:** Bellman: an optimal policy has the property that, whatever the initial state and first decision, the remaining decisions must be optimal with respect to the state resulting from the first decision. Stage $j$ is one decision step ($n$ variables $=$ $n$ stages); decision $u_j$ with return $f_j(u_j)$; state $x_j$ is resource used/available up to stage $j$; transformation $x_{j-1} = t_j(x_j, u_j)$ (sums: $x_{j-1} = x_j - a_j u_j$; products: $x_{j-1} = x_j/u_j$); backward recursion $F_j(x_j) = \mathrm{opt}_{u_j}[f_j(u_j) + F_{j-1}(x_{j-1})]$, $F_1(x_1) = f_1(u_1)$. **Answer:** As stated.

**Q10. Given:** Lec 28 loop and MODI procedure. **Steps:** A loop is a cell sequence where consecutive cells share a row or column, no three consecutive share a row/column, first and last share a row/column, and no cell repeats (a row/column may hold more than two loop cells total, but at most two consecutively). If some non-basic $r_{ij} < 0$, form its unique loop with basic cells, shift $\theta$ (minimum allocation at minus corners) alternately around it, and re-test with MODI until all $r_{ij} \ge 0$. If occupied cells are fewer than $m+n-1$ (simultaneous row/column exhaustion), add an $\epsilon$ zero allocation in the cheapest independent cell forming no loop before running MODI. **Answer:** As stated.

(End of file - total 10 questions + key + solutions)
