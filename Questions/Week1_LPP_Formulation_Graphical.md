# Week 1: LPP Formulation and Graphical Method (Lectures 1-5)

Coverage: OR models and LP formulation, 2-variable graphical method with 4 outcomes, convex sets, simplex standard form and tableau.

## Questions

**Q1 (MCQ).** Which statement about the general optimization model is FALSE?

(a) The three components are decision variables, objective function, and constraints.
(b) A problem with all linear $f, g_k, h_j$ is a linear programming problem; if any one is nonlinear it is nonlinear programming.
(c) An integer programming problem restricts decision variables to integer values.
(d) A linear programming problem requires the number of constraints $m$ to equal the number of variables $n$.

**Q2 (MCQ).** *Source: Lecture 1 quiz/exercise* Hat-profit formulation exercise: a company makes two hat types; type-1 needs twice the labour of type-2; all-type-2 capacity is 500 hats/day; sales limits 150 (type-1) and 250 (type-2); profits Rs 8 and Rs 5. Let $x_1, x_2$ be hats of type 1, 2 per day. The correct LPP is:

(a) Max $z = 8x_1 + 5x_2$ s.t. $2x_1 + x_2 \leq 500$, $x_1 \leq 150$, $x_2 \leq 250$, $x_1, x_2 \geq 0$ integer.
(b) Max $z = 5x_1 + 8x_2$ s.t. $x_1 + 2x_2 \leq 500$, $x_1 \leq 150$, $x_2 \leq 250$, $x_1, x_2 \geq 0$ integer.
(c) Min $z = 8x_1 + 5x_2$ s.t. $2x_1 + x_2 \geq 500$, $x_1 \leq 150$, $x_2 \leq 250$, $x_1, x_2 \geq 0$.
(d) Max $z = 8x_1 + 5x_2$ s.t. $x_1 + x_2 \leq 500$, $x_1 \leq 150$, $x_2 \leq 250$, $x_1, x_2 \geq 0$.

**Q3 (MCQ).** *Source: Lecture 3 quiz/exercise* Max $z = 5x_1 + 3x_2$ s.t. $x_1 + x_2 \leq 5$, $3x_1 + 8x_2 \leq 24$, $x_1, x_2 \geq 0$. The optimum is:

(a) $(0,3)$, $z = 9$
(b) $(16/5, 9/5)$, $z = 21.4$
(c) $(5,0)$, $z = 25$
(d) $(0,0)$, $z = 0$

**Q4 (MCQ).** *Source: Lecture 4 quiz/exercise* Which set is convex?

(a) $S = \{(x,y) : 3x^2 + 2y^2 \leq 6\}$
(b) $S = \{X : |X| = 1\}$
(c) $S = \{(x_1,x_2) : x_1^2 + x_2^2 \leq 4\} \cup \{(10,10)\}$
(d) Union of two disjoint closed discs

**Q5 (MCQ).** In the simplex tableau for a Max problem, with deviation row $\bar{c}_j = c_j - c_B^T P_j$:

(a) Entering variable: smallest $\bar{c}_j$; leaving: largest ratio $b_i / p_{ik}$ over all rows.
(b) Entering variable: largest positive $\bar{c}_j$ (tie: smallest subscript); leaving: minimum ratio $b_i / p_{ik}$ over $p_{ik} > 0$ only.
(c) Entering variable: any negative $\bar{c}_j$; leaving: minimum ratio over all rows including $p_{ik} \leq 0$.
(d) Stop when some $\bar{c}_j > 0$; pivot column entries need not be checked.

**Q6 (Numerical).** *Source: Lecture 3 quiz/exercise* Solve graphically: Max $5x + 8y$ s.t. $3x + 2y \leq 36$, $3x + 4y \geq 24$, $x, y \geq 0$. Give the optimum point and optimum value.

**Q7 (Numerical).** *Source: Lecture 5 quiz/exercise* Solve by simplex: Max $x_1 + x_2 + x_3$ s.t. $3x_1 + 2x_2 + x_3 \leq 3$, $2x_1 + x_2 + 2x_3 \leq 2$, $x_1, x_2, x_3 \geq 0$. Give the optimum point and optimum value.

**Q8 (Numerical).** *Source: Lecture 3 quiz/exercise* Min $5x + 2y$ s.t. $x + 4y \geq 4$, $5x + 2y \geq 10$, $x, y \geq 0$. The objective slope equals the second-constraint slope. Give the minimum value and describe the solution set.

**Q9 (Short answer).** State the two LPP convexity theorems (feasible domain convexity; optimum location) and explain in 2-4 sentences why the simplex method only needs to examine vertices (BFSs).

**Q10 (Short answer).** *Source: Lecture 5 quiz/exercise* Convert to standard form: Min $x_1 - 3x_2 + 3x_3$ s.t. $3x_1 - x_2 + 2x_3 \leq 7$, $2x_1 + 4x_2 \geq -12$, $-4x_1 + 3x_2 + 8x_3 \leq 10$, $x_1, x_2 \geq 0$, $x_3$ unrestricted. Show each conversion step.

## Answer key

| Q | Answer |
|---|---|
| Q1 | (d) |
| Q2 | (a) |
| Q3 | (c) |
| Q4 | (a) |
| Q5 | (b) |
| Q6 | $(0,18)$, max $144$ |
| Q7 | $(0, 4/3, 1/3)$, max $5/3$ |
| Q8 | Min $10$ on segment $(0,5)$-$(16/9, 5/9)$ |
| Q9 | T13 (feasible set convex) + T12 (optimum at vertex/edge); simplex moves vertex to vertex |
| Q10 | Max $-x_1 + 3x_2 - 3x_4 + 3x_5$ s.t. equalities, RHS $\geq 0$, $x_3 = x_4 - x_5$ (see solution) |

## Worked solutions

**Q1. Given:** general model Min/Max $f(X)$, $X \in S \subseteq R^n$. **Steps:** Components per Lecture 1 are exactly (a). Linear vs nonlinear classification is (b). Integer restriction is (c). The LPP definition states $m, n$ positive integers with generally $m \neq n$, so (d) is false. **Answer:** (d).

**Q2. Given:** labour ratio 2:1, capacity 500 type-2 equivalents, bounds 150/250, profits 8/5. **Steps:** $x_1$ type-1 hats consume 2 units each, $x_2$ consume 1: $2x_1 + x_2 \leq 500$. Add $x_1 \leq 150$, $x_2 \leq 250$, Max $8x_1 + 5x_2$, integer non-negative. Option (b) swaps profits and coefficients; (c) minimizes with wrong sense; (d) uses unit coefficients. **Answer:** (a).

**Q3. Given:** Max $5x_1 + 3x_2$, lines $x_1 + x_2 = 5$ through $(0,5),(5,0)$ and $3x_1 + 8x_2 = 24$ through $(0,3),(8,0)$, feasible below both. **Steps:** Corners $O(0,0)$, $A(0,3)$, $B(16/5,9/5)$, $C(5,0)$; $z$: $0, 9, 5(16/5)+3(9/5) = 16+27/5 = 21.4, 25$. Farthest iso-line from origin touches $C$. **Answer:** (c) $(5,0)$, $25$.

**Q4. Given:** Lecture 4 exercise sets. **Steps:** (a) is an ellipse interior $3x^2+2y^2 \leq 6$, a sublevel set of a convex quadratic, hence convex. (b) is the unit sphere $|X|=1$: midpoint of two distinct points has norm $< 1$, leaving the set. (c) adds isolated $(10,10)$ to a disc: segment from disc to $(10,10)$ leaves the set. (d) union of disjoint discs: cross-segment leaves the union. **Answer:** (a).

**Q5. Given:** Max tableau algorithm. **Steps:** Optimality is all $\bar{c}_j \leq 0$; improvement needs $\bar{c}_k > 0$, largest first (tie: smallest subscript). Ratio test uses $b_i/p_{ik}$ only for $p_{ik} > 0$; ignoring $\leq 0$ entries. (a) reverses both rules; (c) enters on negative and uses all rows; (d) states the stop condition backwards. **Answer:** (b).

**Q6. Given:** Max $5x+8y$, $3x+2y \leq 36$, $3x+4y \geq 24$, $x,y \geq 0$. **Steps:** Line 1 through $(12,0),(0,18)$, feasible below (origin satisfies $0 \leq 36$). Line 2 through $(8,0),(0,6)$, feasible above (origin $0 \geq 24$ false). The two lines meet at $y = -6$, outside the first quadrant, so corners are $(8,0),(12,0),(0,18),(0,6)$ with $z$: $40, 60, 144, 48$. **Answer:** $(0,18)$, max $144$.

**Q7. Given:** Max $x_1+x_2+x_3$ with two $\leq$ constraints. **Steps:** Add slacks $x_4, x_5$; BFS $x_4=3,x_5=2$. Iter 1: deviations $(1,1,1,0,0)$, enter $x_1$ (tie, smallest index), ratios $3/3 = 2/2 = 1$, leave $x_4$. Pivot to basis $(x_1,x_5)$. Iter 2: deviations $(0,1/3,2/3,-1/3,0)$, enter $x_3$, ratios $1/(1/3)=3$, $0/(4/3)=0$, leave $x_5$. Iter 3: basis $(x_1,x_3)$, deviation of $x_2$ is $+1/2$, enter $x_2$, only positive pivot entry $3/4$, leave $x_4$. Final basis $(x_2=4/3,x_3=1/3)$, deviations $(-2/3,0,0,-1/3,-1/3) \leq 0$. Check: $3(0)+2(4/3)+1/3 = 3$, $0+4/3+2/3 = 2$. Dual check $y_1=y_2=1/3$ gives $3y_1+2y_2 = 5/3$. **Answer:** $(0,4/3,1/3)$, max $5/3$.

**Q8. Given:** Min $5x+2y$, $x+4y \geq 4$, $5x+2y \geq 10$. **Steps:** Objective gradient $(5,2)$ is parallel to second constraint, so multiples expected. Points $(0,5)$: $0+20 \geq 4$, $0+10 \geq 10$; $(16/9,5/9)$: $16/9+20/9 = 4$, $80/9+10/9 = 10$; both give $z = 10$. Any convex combination $\lambda(0,5)+(1-\lambda)(16/9,5/9)$ lies on $5x+2y=10$ and satisfies the first constraint, giving $z=10$. **Answer:** min $10$ on the whole segment $(0,5)$-$(16/9,5/9)$.

**Q9. Given:** Theorems T13 and T12. **Steps:** T13: $\{X : AX \leq b, X \geq 0\}$ is convex (intersection of half-spaces). T12: if an optimum exists it lies on a vertex or an edge. Since every BFS is a vertex and every edge joins two vertices with all intermediate points as convex combinations sharing the same $z$, checking vertices finds the optimum; the simplex pivots from one adjacent BFS to a better one until deviations certify optimality. **Answer:** as stated.

**Q10. Given:** Min problem with mixed constraints and free $x_3$. **Steps:** (i) Objective: Max $-x_1 + 3x_2 - 3x_3$. (ii) Row 2 RHS $-12 < 0$: multiply by $-1$ to get $-2x_1 - 4x_2 \leq 12$. (iii) Rows 1, 3 ($\leq$): add slacks $x_6, x_7$; converted row 2 ($\leq$): add slack $x_8$. (iv) Free $x_3 = x_4 - x_5$, $x_4, x_5 \geq 0$, substituted everywhere. **Answer:** Max $-x_1 + 3x_2 - 3x_4 + 3x_5$ s.t. $3x_1 - x_2 + 2x_4 - 2x_5 + x_6 = 7$, $-2x_1 - 4x_2 + x_8 = 12$, $-4x_1 + 3x_2 + 8x_4 - 8x_5 + x_7 = 10$, all variables $\geq 0$.
