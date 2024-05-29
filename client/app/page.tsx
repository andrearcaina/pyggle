'use client';
import { Form, Result } from '@/components';
import { DataType } from '@/types/types';
import { useState } from 'react';
import Image from 'next/image';

export default function Home() {
  const [data, setData] = useState<DataType | undefined>(undefined);

  return (
      <main className={"bg-slate-500 min-h-[95vh]"}>
        <div className={"flex justify-center items-center"}>
          <Image
              alt={"Logo"}
              src={"/pyggle_logo.png"}
              width={350}
              height={350}>
          </Image>
        </div>

        <Form setData={setData} />

        <Result output={data} />
      </main>
  );
}
