package com.example.jctree;

import java.util.Vector;

/**������
 * @author��Dyl
 *
 */
public class Main {

	/**
	 * @param args
	 * @throws Exception 
	 */
	public static void main(String[] args) throws Exception {
		//��ȡ����
		File file=new File();
		String urlTest="/data/test.txt";
		String urlPredict="/data/predict.txt";
		Vector<Object> shuXing=file.getShuXing(urlTest);// ��ȡ����
		Vector<Object>[] testDate=file.readData(urlTest);//��ȡ��������-������ͷ����
		Vector<Object[]> predictData=file.readPredictData(urlPredict);//��ȡ��������
		file=null;
		//����
		TreeNode rootNode=JCTree.createTree(shuXing,testDate);
		//��ӡ���ṹ
		System.out.println("�������ṹ���£� ");
		JCTree.showTree(rootNode,0);
		//������Եĳɹ���
		System.out.print("\n�������ĳɹ���Ϊ�� ");
		double temp=0;
		temp=JCTree.suceessGl(rootNode,shuXing,predictData);
		System.out.println((float)temp*1000/10+"%");
	}
}
