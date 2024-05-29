import { Footer } from '@/components';
import './globals.css';

export const metadata = {
  title: 'Pyggle',
  description: 'a web app that solves boggle :)'
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="font-mono">
        <main className="space-y-20">{children}</main>
        <Footer />
      </body>
    </html>
  )
};