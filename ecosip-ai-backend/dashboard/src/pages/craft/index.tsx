/* eslint-disable @next/next/link-passhref */
/* eslint-disable @next/next/no-img-element */
import Link from 'next/link';
import * as React from 'react';

import Layout from '@/components/layout/Layout';
import Seo from '@/components/Seo';
import SectionText from '@/components/Text/SectionText';

import useCraft from '@/store/CraftStore';

const products = [
  {
    id: 1,
    name: 'Smart Recycling Assistant',
    href: 'https://ecosip-ai-smart-recycling-bot.streamlit.app/',
    coin: 'AI Recycle Bot App',
    imageSrc: 'project (3).png',
    imageAlt:
      '',
  },
  {
    id: 2,
    name: 'Eco Impact Tracker',
    href: 'https://ecosip-ai-eco-impact-tracker.streamlit.app/',
    coin: 'Eco Sustainability Coins Calculator App: GreenRewards',
    imageSrc: 'project (2).png',
    imageAlt:
      '',
  },
  {
    id: 3,
    name: 'Carbon Emissions Calculator',
    href: 'https://ecosip-ai-carbon-footprint-tracker.streamlit.app/',
    coin: 'Find out your personal CO2 Footprint',
    imageSrc: 'project (1).png',
    imageAlt:
      '',
  },
];

export default function CraftPage() {

  const crafts = products; 

  return (
    <Layout>
      <Seo templateTitle="Home" />
      <main>
        <section>
          <div className="flex flex-row-reverse flex-wrap">
            <div className="top-0 self-start w-full lg:sticky lg:mt-0 lg:w-4/12 lg:pl-4">
              <div className="relative h-40 bg-bottom bg-no-repeat bg-cover lg:h-96 bg-craft rounded-3xl">
                <div className="absolute top-0 bottom-0 left-0 right-0 z-10 w-full h-full p-6 text-white lg:text-black">
                  <h3>Build Projects</h3>
                  <p className="">and discover your interest!</p>
                </div>
                <div className="w-full h-full bg-gradient-to-b from-gray-700/60 lg:from-transparent to-transparent rounded-3xl"></div>
              </div>
            </div>
            <div className="w-full p-6 text-white bg-gray-800 lg:w-8/12 rounded-3xl">
              <SectionText
                title={'Projects🧾'}
                subTitle={`3 projects available for you!`}
              />
              <div className="">
                <h2 className="sr-only">Products</h2>
                <div className="grid grid-cols-1 gap-y-10 sm:grid-cols-2 gap-x-6 xl:gap-x-8">
                  {crafts.map((product) => (
                    <div key={product.id} className="group">
                      <Link href={product.href} passHref>
                        <a target="_blank" rel="noopener noreferrer">
                          <div>
                            <div className="overflow-hidden bg-gray-200 rounded-3xl aspect-w-1 aspect-h-1 group-hover:opacity-75">
                              <img
                                src={product.imageSrc}
                                alt={product.imageAlt}
                                className="object-cover object-center w-full h-full"
                              />
                            </div>
                            <h4 className="mt-4 text-white">{product.name}</h4>
                            <p className="flex items-center gap-2 mt-1 font-medium text-white">
                              {product.coin}
                            </p>
                          </div>
                        </a>
                      </Link>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>
        </section>
      </main>
    </Layout>
  );
}
