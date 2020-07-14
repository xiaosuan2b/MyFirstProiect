/**
 * 这大概是本项目唯一的一条注释了。
 * 哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈
 * 计算器硝酸版 V1.1.2
 */

//声明区
import java.util.Scanner;
/**
 * @author 硝酸2b
 *
 */
public class minicalc {

	
	//输入区
	/**
	 * @param args
	 */
	static int a;//参与运算的第一个数字
	static int b;//参与运算的第二个数字
	static int way;//运算的方式
	private static String way2;
	public static void main(String[] args) {
		System.out.println("欢迎使用硝酸计算器！V1.1.2");
		
		Scanner input=new Scanner(System.in);
		 System.out.println("请输入你所要参与运算的第一个数字：");
		 a=input.nextInt();//获取a的值
		 
		 System.out.println("请输入你所要运算的方式：");
		 System.out.println("1为加\n2为减\n3为乘\n4为除");
		 way=input.nextInt();//获取运算方式
		 while((way>4)||(way<=0)){
			System.out.println("您输入的运算方式错误，请重新输入：");
			 way=input.nextInt();//获取正确 的运算方式
				 
		 } 
		 
		 System.out.println("请输入你所要参与运算的第二个数字：");
		 b=input.nextInt();//获取第二个数
		 
		 
		 
		//运算区
		 int calcout=0;//声明输出量
		 int yushu=0;//声明余数
		if(way==1) {
			calcout=a+b;
			way2="加法";
		}else if(way==2) {
			calcout=a-b;
			way2="减法";
		}else if(way==3) {
			calcout=a*b;
			way2="乘法";
		}else if(way==4) {
			while(b==0){
				System.out.println("除数不能为零！！！请输入正确的除数：");
				 b=input.nextInt();//获取正确除数
					 
			 } 
			calcout=a/b;
			way2="除法";
		   yushu=a%b;
		}
		
		
		//输出区
		System.out.println(a+"和"+b+"两数进行"+way2+"运算的结果是："+calcout);
		if (yushu!=0) {
			System.out.println("余数为："+yushu);
		}
		
		
	}
		
		
		

	}


/*   BY 
 *      —— ——
 *
 *
 *         ──────── ╲ ┆  ╱    ┄┄┄┄┄   ╱    ╲
 *            ╱              ╲┆╱                ┆  ┆                         ━━━━━
 *          ╱┈┈         ┄┄┄┄            ┏┳━┳┓                      ╱   ╲
 *        ╱┊    ┊        ┆┄┄┄┆           │ ┫  ┣│                 ╱━━━╱
 *          ┊    ┊       ┆┄┄┄┆           │       │                       ╲  ╱
 *           ┈┈┈     ┆┄┄┄┆           │       │                         ╳
 *                             ───────       ╱  ╲
 *
 *                               ╓━━━╕
 *             ━━━━━━━╗                │         ╣
 *                         ╱             │        ╜
 *                       ╱                  │     ╠ 
 *                      ╱                    │        ╖
 *                    ╱                        │         ╣
 *                 ╱                               │        ╜
 *                ╱                                 │       ╛
 *              ┗━━━━━━                ╰━━╝
 *
 *
 *更新日志：
 *  V0.1.1 Beta版本，具备基本功能
 *  V1.1.1 加减乘除样样精通，
 *  V1.1.2 修复了运算方式输入 其他数字结果0的bug
 *		   修复了除数为0时的bug
 *
 *
 *
 *
 *
 */

