# Week 7: Sequencing — n x 2, n x 3, 2 x m, n x m (Lectures 31-35)

Coverage: sequencing terminology (processing order, processing/idle/elapsed time, no-passing rule, assumptions), Johnson's rule for $n$ jobs x $2$ machines with tie-breaking, $n$ x $3$ reduction (conditions, $G=A+B$, $H=B+C$), $2$ x $m$ graphical method ($45^{\circ}$ path, conflict blocks, idle accounting), $n$ x $m$ reduction (dominance conditions, $G=\sum_{1}^{m-1}$, $H=\sum_{2}^{m}$), alternate optima (same $T$, different per-machine idle).

Q1-Q5 are single-correct MCQ. Q6-Q8 expect a number (with unit). Q9-Q10 are short answer (2-4 sentences or a small derivation).

---

## Questions

**Q1.** _____ is the order in which a job has to be processed on different machines. *Source: Lecture 35 quiz Q1*

(a) Idle time
(b) Processing order
(c) Total elapsed time
(d) No-passing rule

**Q2.** An $n$ jobs x $3$ machines problem (order ABC) can be reduced to two fictitious machines only if: *Source: Lecture 35 quiz Q5 (also Lecture 32)*

(a) $\min_i A_i \ge \max_i B_i$ or $\min_i C_i \ge \max_i B_i$
(b) $\min_i B_i \ge \max_i A_i$ or $\min_i B_i \ge \max_i C_i$
(c) $\sum_i A_i = \sum_i B_i = \sum_i C_i$
(d) $\max_i A_i \le \min_i B_i$ and $\max_i C_i \le \min_i B_i$

**Q3.** In the graphical method for $2$ jobs x $m$ machines, moving to the right (horizontal segment) means: *Source: Lecture 35 quiz Q9 (also Lecture 33)*

(a) both jobs are processing simultaneously
(b) job 1 is processing while job 2 is idle
(c) job 2 is processing while job 1 is idle
(d) both jobs are idle

**Q4.** Under Johnson's rule for $n$ jobs x $2$ machines (order AB), if the overall minimum processing time is $B_r$ (on machine B for job $r$), then:

(a) job $r$ is placed first
(b) job $r$ is placed last
(c) job $r$ is deleted from the problem
(d) job $r$ is placed in the middle

**Q5.** The six alternate optimum sequences of the Lecture 32 $n$ x $3$ example give: *Source: Lecture 32 exercise / Lecture 35 quiz Q6-Q7*

(a) different total elapsed times but equal per-machine idle times
(b) the same total elapsed time but different per-machine idle times
(c) the same total elapsed time and the same per-machine idle times
(d) different total elapsed times and different per-machine idle times

**Q6.** Five jobs through machines A then B have times (hours) $A=[5,1,9,3,10]$, $B=[2,6,7,8,4]$. Using Johnson's rule, the minimum total elapsed time $T$ is _____ hours. *Source: Lecture 31 worked example*

**Q7.** Four jobs through machines A, B, C (order ABC) have times $A=[7,9,5,8]$, $B=[2,3,1,4]$, $C=[6,8,7,5]$. After checking the reducibility condition and solving via $G=A+B$, $H=B+C$, the minimum total elapsed time $T$ is _____ hours.

**Q8.** Three jobs (1, 2, 3) through machines $M_1 \to M_4$ have times $M_1=[9,12,7]$, $M_2=[2,3,1]$, $M_3=[3,2,4]$, $M_4=[10,6,9]$. After checking the $n$ x $m$ dominance conditions and solving via fictitious $G, H$, the minimum total elapsed time $T$ is _____ hours.

**Q9.** Distinguish sequencing from scheduling in 2-4 sentences. *Source: Lecture 35 quiz Q15* Give the definition of each and state what a schedule reports beyond the sequence.

**Q10.** A $4$ jobs x $6$ machines problem satisfies $\min T_{1j} \ge \max T_{ij}$ and $\min T_{6j} \ge \max T_{ij}$ for all intermediate $i$. Write the formulas for the fictitious machines $G, H$ and state how the optimal sequence is then obtained. What must you conclude if neither dominance condition holds?

---

## Answer key

| Q | Answer |
|---|---|
| Q1 | (b) Processing order |
| Q2 | (a) |
| Q3 | (b) |
| Q4 | (b) |
| Q5 | (b) |
| Q6 | $30$ hours |
| Q7 | $37$ hours (sequence 3-2-4-1) |
| Q8 | $39$ hours (one optimum: 3-1-2) |
| Q9 | Sequencing = order of jobs; scheduling = elapsed/idle-time plan (see solution) |
| Q10 | $G_j=\sum_{i=1}^{5}T_{ij}$, $H_j=\sum_{i=2}^{6}T_{ij}$, Johnson on G/H; else method fails |

---

## Worked solutions

**Q1. Given:** Lecture 35 definition quiz. **Steps:** Processing order is defined as the order in which a job is processed on the different machines (e.g. ABC for cloth: weave, starch, print); idle time and elapsed time are durations, no-passing is the same-sequence rule. **Answer:** (b).

**Q2. Given:** $n$ x $3$ reducibility theorem (Lecture 32). **Steps:** Reduction $G_i=A_i+B_i$, $H_i=B_i+C_i$ plus Johnson is valid only if the middle machine is dominated: $\min A \ge \max B$ or $\min C \ge \max B$ (either suffices). Options (b)/(d) reverse the inequality; (c) is irrelevant. **Answer:** (a).

**Q3. Given:** Graphical-method conventions (Lectures 33, 35). **Steps:** X-axis = job 1 cumulative time, Y-axis = job 2. Horizontal motion advances only job 1's clock, so job 1 processes while job 2 idles; vertical = reverse; diagonal ($45^{\circ}$) = both process. **Answer:** (b).

**Q4. Given:** Johnson's rule steps (Lecture 31). **Steps:** Global minimum each round: $A_k \to$ job $k$ first (front fill); $B_r \to$ job $r$ last (rear fill); $A_k=B_r$ tie $\to$ $k$ first and $r$ last. Since the minimum sits on B, rear placement keeps B fed without waiting. **Answer:** (b).

**Q5. Given:** Lecture 32 lists six optima (e.g. 3-2-1-4-5, 3-2-4-1-5, ...) all with $T=51$ h; Lecture 35 Q6-Q7. **Steps:** Ties in Johnson's rule branch into alternate optima; chaining in/out shows every branch finishes together ($T$ identical) but head/tail gaps fall on different machines. Hence "same elapsed, different individual idle" = False to both "different elapsed" and "equal idle". **Answer:** (b).

**Q6. Given:** $A=[5,1,9,3,10]$, $B=[2,6,7,8,4]$, order AB. **Steps:** Johnson: $\min=1=A_2 \to$ job 2 first $[2,\_,\_,\_,\_]$; $\min=2=B_1 \to$ job 1 last $[2,\_,\_,\_,1]$; $\min=3=A_4 \to$ job 4 second $[2,4,\_,\_,1]$; $\min=4=B_5 \to$ job 5 fourth $[2,4,\_,5,1]$; job 3 middle $\to$ 2-4-3-5-1. Chain in/out: J2 A 0-1, B 1-7; J4 A 1-4, B 7-15; J3 A 4-13, B 15-22; J5 A 13-23, B 23-27; J1 A 23-28, B 28-30. **Answer:** $T=30$ h (A idle $2$ h tail; B idle $3$ h: 0-1, 22-23, 27-28).

**Q7. Given:** $A=[7,9,5,8]$, $B=[2,3,1,4]$, $C=[6,8,7,5]$. **Steps:** $\min A=5$, $\max B=4$, $\min C=5$; $5 \ge 4$ holds (both conditions hold), so reduce: $G=A+B=[9,12,6,12]$, $H=B+C=[8,11,8,9]$. Johnson on G/H: $\min=6=G_3 \to$ job 3 first; remaining $\min=8=H_1 \to$ job 1 last $[3,\_,\_,1]$; of jobs 2,4 $\min=9=H_4 \to$ job 4 third $[3,\_,4,1]$; job 2 middle $\to$ 3-2-4-1. Chaining A/B/C in-out from $t=0$ ends on C at $37$. Check: $\sum A=29$, $\sum B=10$, $\sum C=26$; exhaustive permutation check confirms $37$ minimal. **Answer:** $T=37$ h with sequence 3-2-4-1.

**Q8. Given:** $M_1=[9,12,7]$, $M_2=[2,3,1]$, $M_3=[3,2,4]$, $M_4=[10,6,9]$. **Steps:** $\min M_1=7$, $\min M_4=6$; $\max M_2=3$, $\max M_3=4$; $7 \ge 3,4$ and $6 \ge 3,4$ both hold. $G_j=M_{1j}+M_{2j}+M_{3j}=[14,17,12]$, $H_j=M_{2j}+M_{3j}+M_{4j}=[15,11,14]$. Johnson: $\min=11=H_2 \to$ job 2 last; of jobs 1,3 $\min=12=G_3 \to$ job 3 first $\to$ 3-1-2. Chaining: J3 $M_1$ 0-7, $M_2$ 7-8, $M_3$ 8-12, $M_4$ 12-21; J1 $M_1$ 7-16, $M_2$ 16-18, $M_3$ 18-21, $M_4$ 21-31; J2 $M_1$ 16-28, $M_2$ 28-31, $M_3$ 31-33, $M_4$ 33-39. **Answer:** $T=39$ h (sequence 3-1-2; 1-3-2 is an alternate optimum with the same $T$).

**Q9. Given:** Lecture 35 Q15. **Steps:** Recall both definitions and the reporting difference. **Answer:** Sequencing is the order in which the jobs are processed on the machines (e.g. 2-4-3-5-1). Scheduling is the time plan built on that sequence: the time-in/time-out table, the total elapsed time $T$ from first start to last finish, and each machine's idle time (head/tail gaps). So sequencing answers "in what order", scheduling answers "when and how long, including idleness".

**Q10. Given:** $n$ x $m$ conditions (Lecture 34), here $m=6$. **Steps:** State $G/H$ sums (all but last / all but first), Johnson finish, failure clause. **Answer:** $G_j=T_{1j}+T_{2j}+\cdots+T_{5j}$ and $H_j=T_{2j}+\cdots+T_{6j}$; solve the $4$ x $2$ problem (G,H) by Johnson's rule and use that sequence for the original $4$ x $6$ problem, then chain in/out to get $T$. If neither $\min T_{1j} \ge \max T_{ij}$ nor $\min T_{6j} \ge \max T_{ij}$ (all intermediate $i$) holds, there is no general Johnson-type procedure and the method fails.
