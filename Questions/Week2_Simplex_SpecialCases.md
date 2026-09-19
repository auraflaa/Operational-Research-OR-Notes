# Week 2: Simplex Special Cases (Lectures 6-10)

Coverage: Big-M and two-phase methods, multiple optima, unboundedness, infeasibility, degeneracy, unrestricted variables, tableau fingerprints.

## Questions

**Q1 (MCQ).** When a Max LPP has a $\geq$ or $=$ row with no unit (basic) column, the Big-M method:

    a) subtracts a surplus variable and stops, since no BFS can ever exist.
    b) adds one artificial variable per such row and penalizes it by $-M$ ($M \to +\infty$) in the Max objective, driving it to zero.
    c) adds one artificial variable per such row with reward $+M$ in the Max objective.
    d) multiplies the RHS by $-1$ and pivots on the surplus column directly.

**Q2 (MCQ).** *Source: Lecture 8 quiz/exercise* Max $6x_1 + 4x_2$ s.t. $2x_1 + 3x_2 \leq 30$, $3x_1 + 2x_2 \leq 24$, $x_1 + x_2 \geq 3$, $x_1, x_2 \geq 0$. Vertex values are $A(0,10)=40$, $B(2.4,8.4)=48$, $C(8,0)=48$, $D(3,0)=18$, $E(0,3)=12$. Which is TRUE?

    a) Unique optimum at $A$ with $z = 40$.
    b) Optimum $48$ attained at $B$ and $C$ and every point of segment $BC$; infinitely many optima.
    c) Optimum $18$ at $D$ since $x_2 = 0$ there.
    d) The problem is infeasible because of the $\geq$ constraint.

**Q3 (MCQ).** *Source: Lecture 9 quiz/exercise* In a Max simplex tableau, for the entering variable $x_k$ ($\bar{c}_k > 0$):

    a) if every pivot-column entry is $\leq 0$ so no ratio can be formed, the problem is unbounded.
    b) if every pivot-column entry is $\leq 0$, the problem is infeasible.
    c) if a non-basic deviation is $0$ at optimum, the problem is unbounded.
    d) if the RHS contains a $0$, the problem is always unbounded.

**Q4 (MCQ).** *Source: Lecture 10 quiz/exercise* A two-phase/Big-M run stops with all deviations $\leq 0$ but an artificial variable is still in basis with positive value. This means:

    a) a degenerate optimum.
    b) multiple optima.
    c) an infeasible problem (no feasible point exists).
    d) an unbounded problem.

**Q5 (MCQ).** *Source: Lecture 6/7 quiz/exercise* Consider Min $x_1 + 2x_2 + x_3$ s.t. $2x_1 + x_2 + x_3 \leq 2$, $3x_1 + 4x_2 + 2x_3 \geq 16$, $x \geq 0$. What is the outcome?

    a) Unique optimum with value $2$.
    b) Multiple optima on an edge.
    c) Unbounded solution.
    d) Infeasible: row 1 caps $3x_1 + 4x_2 + 2x_3$ at $8 < 16$.

**Q6 (Numerical).** *Source: Lecture 6/7 quiz/exercise* Min $z = -3x_1 + x_2 + x_3$ s.t. $x_1 - 2x_2 + x_3 \leq 11$, $-4x_1 + x_2 + 2x_3 \geq 3$, $2x_1 - x_3 = -1$, $x \geq 0$. Solve via Big-M or two-phase (Max $3x_1 - x_2 - x_3$). Give the optimum point and the Min value.

**Q7 (Numerical).** *Source: Lecture 9 quiz/exercise* Max $6x_1 - 2x_2$ s.t. $x_1 - x_2 \leq 1$, $3x_1 - x_2 \leq 6$, $x_1, x_2 \geq 0$. The region is open upward. Give the optimum value and the solution set.

**Q8 (Numerical).** *Source: Lecture 10 quiz/exercise* Phase-1 run of Max $5x_1 - x_2$ s.t. $2x_1 + 3x_2 \leq 6$, $5x_1 + 4x_2 \geq 20$: after entering $x_1$ and leaving $x_3$, deviations are $(0, -7/2, -5/2, -1, 0)$. What is the value of the artificial variable $x_5$ in basis at this stopping table, and what does it certify?

**Q9 (Short answer).** *Source: Lecture 6/7 quiz/exercise* Prove the LPP in Q5 is infeasible with a 2-4 sentence bound argument (no tableau needed).

**Q10 (Short answer).** Define degeneracy graphically and in the tableau, state how an unrestricted (free) variable is handled, and give the two tie-breaking tips from Lecture 10.

## Answer key

| Q | Answer |
|---|---|
| Q1 | (b) |
| Q2 | (b) |
| Q3 | (a) |
| Q4 | (c) |
| Q5 | (d) |
| Q6 | $(4, 1, 9)$, Min $-2$ (Max $2$) |
| Q7 | Max $12$ on ray $(t, 3t - 6)$, $t \geq 5/2$ |
| Q8 | $x_5 = 5 > 0$; certifies infeasibility |
| Q9 | Row 1 forces row-2 LHS $\leq 8 < 16$; hence infeasible |
| Q10 | 3+ constraints concurrent at a vertex; RHS $0$; free $x = x' - x''$; smallest subscript / arbitrary ratio tie |

## Worked solutions

**Q1. Given:** $\geq$/$=$ rows lack a starting unit column after slack/surplus. **Steps:** Surplus subtraction $(-x_5)$ gives no unit column, so one artificial per such row supplies the initial BFS. To force it out, penalize by $-M$ in a Max objective (maximizer drives $-Mx_a$ to $0$). (a) is wrong because the method continues; (c) has the wrong sign; (d) describes no valid pivot. **Answer:** (b).

**Q2. Given:** vertex table from Lecture 8. **Steps:** Highest value $48$ occurs at both $B(2.4,8.4)$ and $C(8,0)$. Objective slope equals second-constraint slope, so the whole edge $BC$ is optimal: $P = \lambda B + (1-\lambda)C$ gives $z = 6(2.4\lambda + 8(1-\lambda)) + 4(8.4\lambda) = 48$. (a)/(c) pick inferior vertices; (d) is false since $B, C$ are feasible. **Answer:** (b).

**Q3. Given:** entering column $k$ with $\bar{c}_k > 0$. **Steps:** Leaving variable needs $\min b_i/p_{ik}$ over $p_{ik} > 0$. If none is positive, $x_k$ can grow to $+\infty$ along a feasible ray with $z \to \infty$. Zero non-basic deviation at optimum signals multiples (not unbounded), and RHS $0$ signals degeneracy. **Answer:** (a).

**Q4. Given:** optimal deviations but artificial still basic and positive. **Steps:** Per Lecture 10, Phase 1 should drive $\sum$ artificials to $0$; a surviving positive artificial means no feasible point satisfies all constraints (worked example: $x_5 = 5$). Degeneracy is RHS $0$; multiples need non-basic zero deviation; unbounded needs ratio failure. **Answer:** (c).

**Q5. Given:** $2x_1 + x_2 + x_3 \leq 2$ vs $3x_1 + 4x_2 + 2x_3 \geq 16$. **Steps:** On $x \geq 0$ with $s = 2x_1+x_2+x_3 \leq 2$, the second LHS per unit of $s$ is best via $x_2$ ($4$ per unit), so LHS $\leq 4 \times 2 = 8 < 16$ (proof in Q9). Hence no feasible point; not unique/multiple/unbounded. **Answer:** (d).

**Q6. Given:** Min $-3x_1+x_2+x_3$; standard Max $3x_1-x_2-x_3$, rows $x_1-2x_2+x_3+x_4=11$, $-4x_1+x_2+2x_3-x_5+x_6=3$, $-2x_1+x_3+x_7=1$. **Steps:** BFS $x_4=11,x_6=3,x_7=1$. T1: deviations $(3-6M, M-1, 3M-1, 0, -M, 0, 0)$; enter $x_3$, ratios $11, 3/2, 1$, leave $x_7$. T2 basis $(x_4,x_6,x_3)$: enter $x_2$, pivot column $(-2,1,0)$, only ratio $1$, leave $x_6$. T3 basis $(x_4=12,x_2=1,x_3=1)$: enter $x_1$, only positive entry $3$, leave $x_4$. T4 basis $(x_1=4,x_2=1,x_3=9)$, all deviations $\leq 0$; artificials out. Max $z = 12-1-9 = 2$. **Answer:** $(4,1,9)$, Min $-2$.

**Q7. Given:** Max $6x_1-2x_2$, region open upward. **Steps:** Corners $O(0,0)=0$, $A(1,0)=6$, $B(5/2,3/2)=15-3=12$. Objective gradient $(6,-2)$ is parallel to binding $3x_1-x_2=6$, so edge points $P(t,3t-6)$ give $z = 6t-6t+12 = 12$ for all $t \geq 5/2$. Iso-lines cannot improve past $12$ despite the open region. **Answer:** max $12$ on ray $(t,3t-6)$, $t \geq 5/2$ (multiple optima, bounded value).

**Q8. Given:** standard rows $2x_1+3x_2+x_3=6$, $5x_1+4x_2-x_4+x_5=20$; Phase-1 Max $-x_5$. **Steps:** T1 deviations $(5,4,0,-1,0)$; enter $x_1$, ratios $6/2=3 < 20/5=4$, leave $x_3$. T2 basis $(x_1=3,x_5=5)$: deviations $(0,-7/2,-5/2,-1,0)$, all $\leq 0$, so Phase 1 stops with $W = -5 \neq 0$. **Answer:** $x_5 = 5 > 0$ in basis; certifies infeasibility (graph: strip below $2x_1+3x_2=6$ misses half-space above $5x_1+4x_2=20$).

**Q9. Given:** Q5 constraints. **Steps:** Let $s = 2x_1+x_2+x_3 \leq 2$. Then $3x_1+4x_2+2x_3 = 2s - x_1 + 2x_2 \leq 2(2) + 2x_2 - x_1$; more directly, per unit of $s$ the LHS earns at most $4$ (via $x_2$), so LHS $\leq 8$ on the first constraint's set, but row 2 demands $\geq 16$. Contradiction. **Answer:** infeasible, no tableau needed.

**Q10. Given:** Lecture 10 tips. **Steps:** Graphically, degeneracy is $3$ or more constraints concurrent at one vertex (example: three lines through $B$ in Max $5x_1+3x_2$ with the extra $9x_1+34x_2 \leq 90$); in the tableau a $0$ appears on the RHS. Free $x$ is replaced by $x = x' - x''$, $x',x'' \geq 0$, in objective and every constraint (one extra variable). Ties: deviation tie enters smallest subscript (fewer iterations); ratio tie leaves arbitrarily (same solution, iteration count may differ). **Answer:** as stated.
