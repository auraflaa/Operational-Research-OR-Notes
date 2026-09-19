# Week 8: Game Theory — Zero-Sum Games to LPP (Lectures 36-40)

Coverage: two-person zero-sum setup (players, strategies, payoff $a_{ij}$ as A's gain = B's loss, assumptions), maximin/minimax, saddle point, pure vs mixed strategies, value $V$ with $\underline{V} \le V \le \overline{V}$, fair vs strictly determinable games, max-min theorems and fundamental theorem, expected payoff $E(X,Y)=X'AY$, dominance (row/column/average), $2 \times 2$ oddments and formulas, $2 \times n$ / $m \times 2$ graphical method (lower/upper envelopes), algebraic method, game-to-LPP conversion ($x_i=p_i/V$, $y_j=q_j/V$, primal-dual pair, constant shift for $V \le 0$ or negative entries).

Q1-Q5 are single-correct MCQ. Q6-Q8 expect a number (exact fraction). Q9-Q10 are short answer (2-4 sentences or a small derivation).

---

## Questions

**Q1.** In a two-person zero-sum game: *Source: Lecture 40 quiz Q2*

(a) both players jointly maximize the total payoff
(b) the gain of one player equals the loss of the other, so the total is zero
(c) the value of the game is always zero
(d) communication between players before play is assumed

**Q2.** "Every matrix game has a saddle point." *Source: Lecture 40 quiz Q3*

(a) True, and pure strategies are then always optimal
(b) True, by the fundamental theorem of rectangular games
(c) False; games without a saddle point are solved by mixed strategies
(d) False; games without a saddle point have no value

**Q3.** A game with maximin = minimax = $0$ is called _____, and a game with maximin = minimax = $V$ (saddle exists) is called _____. *Source: Lecture 40 quiz Q10-Q11 (also Lecture 36)*

(a) strictly determinable; fair
(b) fair; strictly determinable
(c) mixed; pure
(d) rectangular; fair

**Q4.** For $A=\begin{pmatrix}a_{11} & a_{12}\\ a_{21} & a_{22}\end{pmatrix}$ with no saddle and $D=a_{11}+a_{22}-a_{12}-a_{21} \ne 0$, the optimal row mix is:

(a) $p_1=(a_{22}-a_{21})/D$, $p_2=1-p_1$
(b) $p_1=(a_{11}-a_{12})/D$, $p_2=1-p_1$
(c) $p_1=(a_{22}-a_{12})/D$, $p_2=1-p_1$
(d) $p_1=a_{11}/(a_{11}+a_{22})$, $p_2=1-p_1$

**Q5.** The graphical method can be used to solve a $4 \times 2$ game. *Source: Lecture 40 quiz Q6*

(a) True — it is in the $m \times 2$ family: plot one line per A-row in $y$ and minimize the upper envelope
(b) True — by plotting four lines and maximizing the lower envelope
(c) False — graphics only works for $2 \times 2$ games
(d) False — graphics only works for $2 \times n$ games

**Q6.** For $A=\begin{pmatrix}1 & 3\\ 10 & 2\end{pmatrix}$ there is no saddle point. The value of the game is $V=$ _____ (exact fraction). *Source: Lecture 38 Case-1 worked example (oddments)*

**Q7.** In the Lecture 39 matching-coins game, A wins $+1$ on (H,H), $0$ on (T,T), loses $1/2$ on mixed pairs, so $A=\begin{pmatrix}1 & -1/2\\ -1/2 & 0\end{pmatrix}$. The value of the game is $V=$ _____ (exact fraction). *Source: Lecture 39 algebraic-method example*

**Q8.** For $A=\begin{pmatrix}4 & 1\\ 2 & 3\end{pmatrix}$, confirm there is no saddle point and compute the value: $V=$ _____ (exact fraction or decimal).

**Q9.** The payoff matrix contains negative entries (and $V \le 0$ is suspected). State the standard fix in 2-4 sentences. *Source: Lecture 40 quiz Q15 (also Lecture 39)* Include what happens to the strategies and to the value.

**Q10.** Write the LPP pair for a general $m \times n$ game after the substitution $x_i=p_i/V$, $y_j=q_j/V$ (assume shifted $V' > 0$). State the primal-dual relationship and which LP is solved in practice and why.

---

## Answer key

| Q | Answer |
|---|---|
| Q1 | (b) |
| Q2 | (c) |
| Q3 | (b) fair; strictly determinable |
| Q4 | (a) |
| Q5 | (a) |
| Q6 | $V=14/5$ ($28/10$) |
| Q7 | $V=-1/8$ |
| Q8 | $V=5/2$ ($2.5$) |
| Q9 | Add constant $k$ to every entry; strategies carry over, $V_{\text{orig}}=V_{\text{new}}-k$ (see solution) |
| Q10 | A: $\min\sum x_i$ s.t. column constraints $\ge 1$; B: $\max\sum y_j$ s.t. row constraints $\le 1$; duals; solve B's $\le$-LP |

---

## Worked solutions

**Q1. Given:** Zero-sum definition (Lectures 36, 40). **Steps:** Zero-sum means A's receipt $a_{ij}$ is exactly B's payment; non-zero total contradicts the definition; value zero is only the fair-game special case; assumption is no communication with simultaneous moves. **Answer:** (b).

**Q2. Given:** Saddle existence (Lectures 36-37, 40). **Steps:** Only pure-strategy (strictly determinable) games have a saddle; e.g. Lecture 36's $3 \times 3$ with maximin $-3 \ne 4=$ minimax has none. The fundamental theorem guarantees a value and optimal (possibly mixed) strategies for every matrix game, not a saddle. **Answer:** (c).

**Q3. Given:** Lecture 36 definitions, Lecture 40 Q10-Q11. **Steps:** Fair requires the common maximin=minimax value to be $0$; strictly determinable requires maximin=minimax=$V$ (saddle exists, $V$ need not be $0$). Lecture 36's Example 1 ($V=-1$) is strictly determinable but not fair. **Answer:** (b).

**Q4. Given:** $2 \times 2$ formula box (Lecture 38). **Steps:** Equating A's expectations against B's columns gives $p_1=(a_{22}-a_{21})/D$; option (c) is the $q_1$ formula $(a_{22}-a_{12})/D$; (b)/(d) are distractors. Oddments gives the same result (difference of the other pair). **Answer:** (a).

**Q5. Given:** Lecture 38 Case 3, Lecture 40 Q6. **Steps:** $4 \times 2$ is $m \times 2$: B mixes $(y,1-y)$, one expected-payoff line per A-row is plotted over $0 \le y \le 1$, and B minimizes the upper envelope (minimax); the intersecting pair reduces to $2 \times 2$. Lower-envelope maximization belongs to $2 \times n$. **Answer:** (a).

**Q6. Given:** $A=\begin{pmatrix}1 & 3\\ 10 & 2\end{pmatrix}$. **Steps:** Row minima $1,2 \to$ maximin $2$; column maxima $10,3 \to$ minimax $3$; unequal, no saddle. Row oddments: $|3-1|=2$ (against row 2), $|10-2|=8$ (against row 1): $p=(8/10,2/10)=(4/5,1/5)$. Column oddments: $|10-1|=9$ (against col 2), $|3-2|=1$ (against col 1): $q=(1/10,9/10)$. Value row-weighted: $V=(1\cdot 8+10\cdot 2)/10=28/10=14/5$ (column check: $(1\cdot 1+3\cdot 9)/10=28/10$). **Answer:** $V=14/5$.

**Q7. Given:** $A=\begin{pmatrix}1 & -1/2\\ -1/2 & 0\end{pmatrix}$, $p_1+p_2=q_1+q_2=1$. **Steps:** Row minima $-1/2,-1/2 \to$ maximin $-1/2$; column maxima $1,0 \to$ minimax $0$; no saddle. A as equations: $p_1-\tfrac12p_2=V$, $-\tfrac12p_1=V$. From the second, $p_1=-2V$; substituting, $-2V-\tfrac12p_2=V$ with $p_2=1-p_1$ gives $-8V=1$, so $V=-1/8$, $p_1=1/4$, $p_2=3/4$. B symmetrically: $q_1-\tfrac12q_2=V$, $-\tfrac12q_1=V$, $q_1+q_2=1 \to q=(1/4,3/4)$, same $V$. **Answer:** $V=-1/8$ (A loses $1/8$ per play on average).

**Q8. Given:** $A=\begin{pmatrix}4 & 1\\ 2 & 3\end{pmatrix}$. **Steps:** Row minima $1,2 \to$ maximin $2$; column maxima $4,3 \to$ minimax $3$; $2 \ne 3$, no saddle. $D=4+3-1-2=4$. $p_1=(3-2)/4=1/4$, $p_2=3/4$; $q_1=(3-1)/4=1/2$, $q_2=1/2$; $V=(4\cdot 3-1\cdot 2)/4=10/4=5/2$. Check rows: $4(1/4)+2(3/4)=5/2$; $1(1/4)+3(3/4)=5/2$. Check columns: $4(1/2)+1(1/2)=5/2$; $2(1/2)+3(1/2)=5/2$. **Answer:** $V=5/2=2.5$.

**Q9. Given:** Negative entries / $V \le 0$ block the $x_i=p_i/V$ division (Lecture 39) — Lecture 40 Q15. **Steps:** Recall shift rule and recovery. **Answer:** Add a constant $k$ to every entry so the smallest entry becomes $0$ (all entries $\ge 0$, shifted value $>0$), then solve. Optimal mixed strategies of the shifted game carry over unchanged to the original game, and the original value is recovered as $V_{\text{original}}=V_{\text{new}}-k$.

**Q10. Given:** Game-to-LP conversion (Lecture 39). **Steps:** Divide the $\ge V$ / $\le V$ systems by $V'>0$ and flip max-$V$ to min-$1/V$. **Answer:** Player A (primal): $\min Z_p=\sum_{i=1}^{m}x_i$ s.t. $\sum_i a_{ij}x_i \ge 1$ for each B-column $j$, $x_i \ge 0$. Player B (dual): $\max Z_q=\sum_{j=1}^{n}y_j$ s.t. $\sum_j a_{ij}y_j \le 1$ for each A-row $i$, $y_j \ge 0$. B's LP is the dual of A's and vice versa, with $Z_p^*=Z_q^*=1/V'$; recover $V'=1/Z^*$, $p_i=x_iV'$, $q_j=y_jV'$, then subtract any shift $k$. In practice solve B's $\le$-LP: it needs only slack variables (no artificials), and A's solution is read from the optimum tableau as the dual — the Lecture 40 ABC/XYZ solve ($y^*=(0,13/360,1/180)$, $V=24$) is exactly this route.
