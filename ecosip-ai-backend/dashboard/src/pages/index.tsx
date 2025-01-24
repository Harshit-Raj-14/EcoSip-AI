import * as React from 'react';

import Layout from '@/components/layout/Layout';
import AchievementSection from '@/components/section/AchievementSection';
import CategorySection from '@/components/section/CategorySection';
// import HistorySection from '@/components/section/HistorySection';
import Seo from '@/components/Seo';
import SectionText from '@/components/Text/SectionText';

export default function HomePage(): JSX.Element {
  return (
    <Layout>
      <Seo templateTitle='Home' />
      <main>
        <section>
          <div className=''>
            <div className='w-full px-8 py-8 bg-gray-800 lg:w-12/14 rounded-3xl'>
              <SectionText title={'Home🍀'} subTitle={'24 January 2025'} />
              <AchievementSection />
              <CategorySection />
            </div>
          </div>
        </section>
      </main>
    </Layout>
  );
}
