public class 论取余会不会改变原数{
	public static void main(String[]args){
		int a=11;
		int b;
		b=a%10;
		System.out.println("a="+a);
		System.out.println("b="+b);
	}
}
/*
*	输出：a=11,b=1
*	结论：不会
*/



/*   BY 
 *      —— ——
 *
 *
 *         ──────── ╲  ┆  ╱            ┄┄┄┄┄   ╱    ╲
 *            ╱      ╲┆╱                ┆  ┆    ━━━━━
 *          ╱┈┈    ┄┄┄┄            ┏┳━┳┓   ╱   ╲
 *        ╱┊    ┊ ┆┄┄┄┆           │ ┫  ┣│    ╱━━━╱
 *          ┊    ┊ ┆┄┄┄┆           │       │      ╲  ╱
 *           ┈┈┈  ┆┄┄┄┆           │       │        ╳
 *                           ╯            ───────       ╱  ╲
 *
 *                                           ╓━━━╕
 *             ━━━━━━━╗                │       ╣
 *                         ╱                │      ╜
 *                       ╱                  │     ╠ 
 *                      ╱                    │      ╖
 *                    ╱                      │       ╣
 *                 ╱                        │      ╜
 *                ╱                          │     ╛
 *              ┗━━━━━━                ╰━━╝
 *
 *
 *
 *
 *
 *
 *
 *
 */
